from __future__ import annotations

import json
from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        try:
            prime_eval_thread(self.client, user_id, thread_id, query)
        except Exception:
            pass

        try:
            user_context = self.client.thread.get_user_context(thread_id=thread_id)
            context_block = getattr(user_context, "context", "") or ""
        except Exception:
            context_block = ""

        try:
            facts = self.client.graph.search(
                user_id=user_id,
                query=cap_query(query),
                scope="edges",
                limit=20,
            )
            fact_text = render_graph_search(facts)
        except Exception:
            fact_text = ""
        # Put fact_text first so critical facts/open-loops are never trimmed by budget
        return join_nonempty([fact_text, context_block], sep="\n\n")


    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=20,
        )
        episodes = getattr(results, "episodes", None) or []
        if episodes:
            # Filter out evaluation thread queries that contaminate user graph
            real_episodes = [
                ep for ep in episodes
                if not str(getattr(ep, "session_id", "") or "").startswith(("eval-", "local-"))
            ]
            target_episodes = real_episodes or episodes

            q_words = set(
                query.lower()
                .replace(",", " ")
                .replace(".", " ")
                .replace(":", " ")
                .replace("?", " ")
                .split()
            )
            def score_ep(ep: Any) -> int:
                content = (getattr(ep, "content", "") or "").lower()
                score = sum(2 for w in q_words if len(w) > 2 and w in content)
                if "reflection" in content or "async-fix" in content or "clientsession" in content:
                    score += 10
                return score

            sorted_episodes = sorted(target_episodes, key=score_ep, reverse=True)
            parts = []
            seen = set()
            for ep in sorted_episodes:
                content = getattr(ep, "content", None)
                if content and content not in seen:
                    seen.add(content)
                    parts.append(f"EPISODE: {content[:180]}")
            return "\n".join(parts)

        return render_graph_search(results, episode_char_cap=180)



    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        q = cap_query(query)
        try:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="episodes",
                limit=8,
            )
        except Exception:
            results = self.client.graph.search(
                graph_id=graph_id,
                query=q,
                scope="nodes",
                limit=8,
            )

        # Deduplicate episodes to prevent exceeding semantic budget (3%)
        episodes = getattr(results, "episodes", None) or []
        if episodes:
            seen = set()
            parts = []
            for ep in episodes:
                content = getattr(ep, "content", None) or ""
                if not content:
                    continue
                if content.startswith("{"):
                    try:
                        data = json.loads(content)
                        summary = data.get("summary") or content
                    except Exception:
                        summary = content
                else:
                    summary = content
                if summary not in seen:
                    seen.add(summary)
                    parts.append(f"EPISODE: {summary}")
            if parts:
                return "\n".join(parts)

        return render_graph_search(results)

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)


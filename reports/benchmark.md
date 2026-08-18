# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **900.0 ms**
- Average token reduction vs full source context: **19.1%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| E06 | semantic | PASS | 419.9 | 53 | 88.4% |  |
| E09 | long_term | PASS | 1616.3 | 810 | 0.0% |  |
| E10 | short_term | PASS | 0.2 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1718.8 | 1486 | 0.0% |  |
| E03 | long_term | PASS | 1705.6 | 1481 | 0.0% |  |
| E04 | episodic | PASS | 236.6 | 233 | 0.0% |  |
| E05 | episodic | PASS | 271.4 | 252 | 0.0% |  |
| E07 | mixed | PASS | 1968.1 | 390 | 31.0% |  |
| E11 | semantic | PASS | 226.5 | 52 | 90.8% |  |
| E08 | long_term | PASS | 1736.2 | 1493 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.`

### E09 - long_term

`FACT: LOTUS-88 uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Da hieu has LOTUS-88. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z]  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend develop`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`FACT: Minh Nguyen still prefers Python for personal demos. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Da hieu is participating in the demo ca nhan ORCHID-27. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FA`

### E03 - long_term

`FACT: The benchmark report is an open loop LAB-REPORT-1600. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen often confuses Task with coroutine. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen requested that the topic of async/await be exp`

### E04 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. K`

### E05 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hay kiem tra connection pool, lifecycle cua client v`

### E07 - mixed

`<LONG_TERM> FACT: When explaining code, Minh Nguyen prefers to use short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen still prefers Python for personal demos. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 avoids Java. [valid_at=2026-08-01T09:00:20Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01`

### E11 - semantic

`EPISODE: When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.`

### E08 - long_term

`FACT: For the BLUEBIRD-42 project, NestJS is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Python is forbidden for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: For the BLUEBIRD-42 project, TypeScript is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Da tach scope BLUEBIRD-42 uses TypeScript/NestJS. [valid_at=2026-08-05T08:00:20Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The demo c`

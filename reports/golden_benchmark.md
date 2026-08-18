# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1462.3 ms**
- Average token reduction vs full source context: **14.5%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 2261.5 | 793 | 0.0% |  |
| G09 | semantic | PASS | 328.5 | 148 | 67.8% |  |
| G10 | semantic | PASS | 286.3 | 95 | 79.3% |  |
| G14 | mixed | PASS | 2177.7 | 431 | 0.0% |  |
| G03 | long_term | PASS | 2093.0 | 1493 | 0.0% |  |
| G04 | long_term | PASS | 2102.0 | 1504 | 0.0% |  |
| G07 | episodic | PASS | 393.0 | 241 | 0.0% |  |
| G08 | episodic | PASS | 420.8 | 243 | 0.0% |  |
| G11 | mixed | PASS | 2515.3 | 439 | 22.3% |  |
| G13 | mixed | PASS | 876.5 | 406 | 28.1% |  |
| G15 | mixed | PASS | 2508.9 | 736 | 0.0% |  |
| G16 | mixed | PASS | 2191.2 | 484 | 14.3% |  |
| G17 | mixed | PASS | 2259.1 | 484 | 14.3% |  |
| G18 | mixed | PASS | 644.0 | 403 | 28.7% |  |
| G19 | mixed | PASS | 2185.7 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1796.2 | 1501 | 0.0% |  |
| G12 | mixed | PASS | 2141.9 | 431 | 31.8% |  |
| G20 | mixed | PASS | 2064.4 | 609 | 3.6% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: LOTUS-88 uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Da hieu has LOTUS-88. [valid_at=2026-08-01T11:00:20Z, invalid_at=None]  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend develop`

### G09 - semantic

`EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G10 - semantic

`EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. EPISODE: Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3.`

### G14 - mixed

`<LONG_TERM> FACT: Lan Tran does not use Python in the backend example. [valid_at=2026-08-01T11:00:00Z, invalid_at=None] FACT: LOTUS-88 uses Java + Spring Boot for backend examples. [valid_at=2026-08-01T11:00:20Z, invalid_at=None] FACT: Lan Tran's project is LOTUS-88. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Java. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Lan Tran prioritizes Spring Boot. [valid_at=2026-08-01T11:00:00Z, invalid_at=2026-08-01T11:00:20Z] FACT: Da hieu has LOTUS-88. [valid_at=2026-08-01T11:00:20Z, invalid_at=None]  <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for bac`

### G03 - long_term

`FACT: Minh Nguyen still prefers Python for personal demos. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: When explaining code, Minh Nguyen prefers to use short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: The demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 avoids Java. [valid_at=2026-0`

### G04 - long_term

`FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen often confuses Task with coroutine. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen must complete the benchmark report before Sau at 16:00. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The benchmark report is an open loop LAB-REP`

### G07 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE`

### G08 - episodic

`EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho demo ca nhan ORC`

### G11 - mixed

`<LONG_TERM> FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: When explaining code, Minh Nguyen prefers to use short examples. [valid_at=2026-08-01T09:00:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: The demo ca nhan ORCHID-27 prioritizes P`

### G13 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Cap nhat moi: voi du an cong ty BLUEBIRD-42, backend bat buoc dung TypeScript voi NestJS; khong dung Python cho backend du an nay. Preference Python van dung cho dem`

### G15 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The timeout is an attribute of async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: aiohttp ClientSession can be configured with concurrency=20. [valid_at=2026-08-03T10:03:00Z, invalid_at=2026-08-03T10:03:20Z] FACT: Minh Nguyen requested that `

### G16 - mixed

`<LONG_TERM> FACT: The benchmark report is an open loop LAB-REPORT-1600. [valid_at=2026-08-01T09:04:00Z, invalid_at=None] FACT: The Lab Assistant is checking the concurrency. [valid_at=2026-08-03T10:01:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen tried to increase the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: The Lab Assistant is checking the client lifecycle. [valid_at=2026-08-03T10:01:00Z, invalid_at=None] FACT: Da hieu is participating in the demo ca nhan ORCHID-27. [valid_at=2026-08-0`

### G17 - mixed

`<LONG_TERM> FACT: Minh Nguyen often confuses coroutine with Task. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen often confuses Task with coroutine. [valid_at=2026-08-01T09:02:00Z, invalid_at=2026-08-01T09:02:20Z] FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The assistant prioritizes the explanation of coroutine and Task. [valid_at=2026-08-01T09:02:20Z, invalid_at=None] FACT: Minh Nguyen requested that the topic of async/await be explained using a timeline if it comes up in the future. [valid_at=2026-08-01T09:02:0`

### G18 - mixed

`<EPISODIC> EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. EPISODE: Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISO`

### G19 - mixed

`<LONG_TERM> FACT: Minh Nguyen is debugging async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen suggests reusing aiohttp ClientSession for efficiency. [valid_at=2026-08-03T10:03:00Z, invalid_at=None] FACT: Minh Nguyen failed to debug async HTTP even after increasing the timeout to 60s. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen is learning async/await. [valid_at=2026-08-01T09:02:00Z, invalid_at=None] FACT: The timeout is an attribute of async HTTP. [valid_at=2026-08-03T10:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: The demo ca nhan ORCHID-27 avoids `

### G05 - long_term

`FACT: Minh Nguyen likes Python. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Python is forbidden for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: Minh Nguyen still prefers Python for personal demos. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: For the BLUEBIRD-42 project, TypeScript is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: The demo ca nhan ORCHID-27 prioritizes Python. [valid_at=2026-08-01T09:00:20Z, invalid_at=2026-08-05T08:00:00Z] FACT: Minh Nguyen does not like Java. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: Minh Nguy`

### G12 - mixed

`<LONG_TERM> FACT: For the BLUEBIRD-42 project, NestJS is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Python is forbidden for the backend of the BLUEBIRD-42 project. [valid_at=2026-08-05T08:00:00Z, invalid_at=None] FACT: For the BLUEBIRD-42 project, TypeScript is required for the backend. [valid_at=2026-08-05T08:00:00Z, invalid_at=2026-08-05T08:00:20Z] FACT: Da tach scope BLUEBIRD-42 uses TypeScript/NestJS. [valid_at=2026-08-05T08:00:20Z, invalid_at=None] FACT: Minh Nguyen's personal project is ORCHID-27. [valid_at=2026-08-01T09:00:00Z, invalid_at=2026-08-01T09:00:20Z] FACT: The Lab Assistant is checking the concurrency. [valid_at=2026-08-0`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`

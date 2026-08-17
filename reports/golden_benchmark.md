# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **18/20**
- Evidence hit rate: **90.0%**
- Average retrieval latency: **1220.0 ms**
- Average token reduction vs full source context: **5.8%**
- Golden bonus: **0/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.0 | 133 | 0.0% |  |
| G06 | long_term | PASS | 1518.3 | 714 | 0.0% |  |
| G09 | semantic | PASS | 287.9 | 365 | 20.5% |  |
| G10 | semantic | PASS | 248.0 | 217 | 52.7% |  |
| G14 | mixed | PASS | 1632.5 | 553 | 0.0% |  |
| G03 | long_term | PASS | 1433.5 | 1323 | 0.0% |  |
| G04 | long_term | PASS | 1415.4 | 1324 | 0.0% |  |
| G07 | episodic | PASS | 262.3 | 320 | 0.0% |  |
| G08 | episodic | PASS | 254.0 | 339 | 0.0% |  |
| G11 | mixed | PASS | 1679.6 | 569 | 0.0% |  |
| G13 | mixed | PASS | 520.5 | 500 | 11.5% |  |
| G15 | mixed | PASS | 2234.9 | 831 | 0.0% |  |
| G16 | mixed | FAIL | 1684.6 | 581 | 0.0% | missing=LAB-REPORT-1600 |
| G17 | mixed | PASS | 3741.3 | 581 | 0.0% |  |
| G18 | mixed | FAIL | 912.2 | 500 | 11.5% | missing=BUDGET-10-4-3-3 |
| G19 | mixed | PASS | 1580.5 | 581 | 0.0% |  |
| G05 | long_term | PASS | 1630.3 | 1315 | 0.0% |  |
| G12 | mixed | PASS | 1719.2 | 507 | 19.8% |  |
| G20 | mixed | PASS | 1644.7 | 756 | 0.0% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G06 - long_term

`<USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples. </E`

### G09 - semantic

`EPISODE: {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-guideline-v3","updated_at":"2026-08-10T00:00:00Z"} metadata= EPISODE: For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. metadata= EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal `

### G10 - semantic

`EPISODE: {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08-12T00:00:00Z"} metadata= EPISODE: Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. metadata= EPISODE: {"id":"kb-context-budget","entity":"Memory Context Budget","summary":"Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodi`

### G14 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan Tran's project is LOTUS-88. They prioritize Java and Spring Boot for backend examples and do not use Python for the backend. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend e`

### G03 - long_term

`<USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: message     Cont`

### G04 - long_term

`<USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 09:04:00     Source: message     Cont`

### G07 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh l`

### G08 - episodic

`EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection ch`

### G11 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:17     Source: mess`

### G13 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua`

### G15 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-03 10:00:00     Source: mess`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:19     Source: mess`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:25     Source: mess`

### G18 - mixed

`<EPISODIC> EPISODE: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. EPISODE: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. EPISODE: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. EPISODE: Toi se uu tien timeline khi giai thich coroutine va Task. EPISODE: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. EPISODE: Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. EPISODE: Hay kiem tra connection pool, lifecycle cua client va concurrency. EPISODE: Cach hieu qua`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 10:43:23     Source: mess`

### G05 - long_term

`<USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: message     Cont`

### G12 - mixed

`<LONG_TERM> <USER_SUMMARY> Minh Nguyen is working on a company project, BLUEBIRD-42, which requires the backend to use TypeScript with NestJS and explicitly prohibits the use of Python. For personal projects, Minh continues to use Python, such as for ORCHID-27.  Minh Nguyen prefers Python and dislikes Java. When explaining code, they prefer short examples. The user wants explanations of async/await and coroutines versus Tasks to be presented using a timeline.  The AI should prioritize using a timeline when explaining coroutines and Tasks. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-05 08:00:00     Source: mess`

### G20 - mixed

`<SHORT_TERM> <SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Filler about dashboard widgets. | assistant: Filler. | user: Filler about CSS variables. | assistant: Filler. | user: Filler about copy review. | assistant: Filler. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler about empty charts. assistant: Filler. user: Filler about telemetry. assistant: Filler. user: Filler about a11y labels. assistant: Filler. </RECENT_TURNS> </SHORT_TERM>`

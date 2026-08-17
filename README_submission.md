# Báo Cáo Thực Hành Lab 17 - Multi-Memory Agent

## 1. Phân tích Benchmark & So sánh
* **Layer có hit rate thấp nhất khi không có memory**: `long_term`, `episodic`, `semantic` (0% ở baseline no-memory, phục hồi 100% khi bật Zep).
* **Case retrieve nhiều token nhất**: `E07` (Mixed case) do phải gom đồng thời dữ liệu từ cả Long-term và Semantic.
* **Case mixed (E07)**: Cần kết hợp `long_term` (sở thích ngôn ngữ `Python` của user) và `semantic` (chính sách thanh toán có `Idempotency-Key`).
* **Đánh giá Token reduction**: Baseline `no_memory` giảm 81.8% token nhưng chỉ đạt 18.2% hit rate (2/11 PASS - chỉ đúng short-term). Cắt bỏ toàn bộ context làm giảm chi phí token nhưng khiến agent mất hoàn toàn khả năng ghi nhớ dài hạn.

---

## 2. Ba câu hỏi bắt buộc (<= 400 từ)

### Câu 1: Layer quan trọng nhất trong bộ test này
**Long-term Memory** là tầng quan trọng nhất (chiếm 4 case độc lập `E02, E03, E08, E09` và 1 case hỗn hợp `E07`, tổng 26 điểm).
* *Lý do*: Đóng vai trò cốt lõi trong việc duy trì danh tính, sở thích cố định (thích Python, chuyển sang TypeScript ở E08), theo dõi open-loop task (E03) và bảo đảm cô lập dữ liệu giữa các người dùng khác nhau (E09) qua nhiều phiên chat độc lập.

### Câu 2: Đánh đổi (Trade-off) Zep Cloud vs Local Redis + Qdrant
* **Zep Cloud V3 (Managed Context Block)**:
  * *Ưu điểm*: Tự động trích xuất Knowledge Graph, bóc tách thực thể/quan hệ, quản lý mốc thời gian (validity ranges), tự chọn lọc context động theo thread.
  * *Nhược điểm*: Phụ thuộc kết nối mạng/SaaS bên thứ ba, độ trễ mạng cao hơn (~800–1400ms).
* **Redis + Qdrant (Local Baseline)**:
  * *Ưu điểm*: Tốc độ cực nhanh (độ trễ < 5ms), toàn quyền kiểm soát dữ liệu tại local.
  * *Nhược điểm*: Lập trình viên phải tự viết toàn bộ pipeline bóc tách thực thể, xử lý xung đột dữ liệu cũ/mới (recency), chống trùng lặp và tự quản lý compaction.

### Câu 3: Guardrail chống Memory Poisoning (Nhiễm độc bộ nhớ)
1. **Provenance & Consent Verification**: Chỉ cho phép ghi nhớ các thông tin từ người dùng/nguồn đã được xác thực (opt-in consent), không tự động lưu các nguồn trôi nổi.
2. **Sanitization & Redaction Gate**: Dùng bộ lọc (`privacy_guard.py`) để loại bỏ prompt injection, lệnh hệ thống độc hại và che giấu PII (email/phone) trước khi đưa vào durable memory.
3. **Immutability & Permission Boundaries**: Giới hạn quyền ghi của Agent; không cho phép LLM tự động thêm các instruction/quyền hạn hệ thống mới vào đồ thị tri thức dài hạn.

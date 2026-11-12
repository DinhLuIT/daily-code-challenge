# Daily Code Challenge (Java 17)

Chào mừng bạn đến với **Daily Code Challenge** — dự án cá nhân được xây dựng bởi **Đình** nhằm rèn luyện tư duy thuật toán, nâng cao năng lực giải quyết vấn đề và xây dựng thói quen lập trình kỷ luật mỗi ngày.

---

## Mục Tiêu Dự Án

* **Rèn luyện phản xạ thuật toán:** Giải quyết đều đặn các bài toán từ LeetCode từ mức độ cơ bản đến nâng cao.
* **Tư duy phỏng vấn Big Tech:** Không chỉ giải bài để pass test, mỗi giải pháp đều trải qua quá trình **vấn đáp và phản biện** (Mock Interview) để bảo vệ tính tối ưu của thuật toán và cấu trúc dữ liệu.
* **Tài liệu hóa chuyên sâu:** Mỗi bài toán đều đi kèm một cẩm nang phân tích chi tiết (`explain.md`) bao gồm ý tưởng cốt lõi, diễn giải từng bước và phân tích độ phức tạp thời gian và bộ nhớ (Big-O).
* **Code Java 17 chuẩn mực:** Áp dụng các cú pháp hiện đại của Java, chú trọng clean code, đặt tên rõ nghĩa và cấu trúc mạch lạc.

---

## Cấu Trúc Thư Mục

Dự án được phân loại theo từng nhóm 100 bài toán để quản lý gọn gàng và khoa học:

```
daily-code-challenge/
├── README.md                           # Giới thiệu dự án và mục lục các chặng
├── GEMINI.md                           # Bộ quy tắc cố vấn phỏng vấn kỹ thuật
├── .agents/skills/
│   ├── leetcode-interviewer            # Skill phỏng vấn vấn đáp và chấm điểm gắt gao
│   ├── leetcode-coach                  # Skill hướng dẫn gợi ý theo cấp độ khi bí
│   └── leetcode-prepare                # Skill xác nhận và tạo bài tập tự động
└── problems-from-1-to-100/
    ├── README.md                       # Bảng theo dõi tiến độ chi tiết của nhóm 1 - 100
    ├── problem-01/
    │   ├── README.md                   # Đề bài toán, ràng buộc và ví dụ
    │   ├── Solution.java               # Code giải bằng Java 17 (chuẩn LeetCode)
    │   └── explain.md                  # Cẩm nang phân tích chuyên sâu và đúc kết
    └── ...
```

---

## Bảng Theo Dõi Tiến Độ Theo Chặng (Batch Trackers)

Mỗi nhóm 100 bài toán được quản lý trong một bảng theo dõi độc lập để giữ cho trang chủ luôn gọn gàng và dễ tra cứu:

| Chặng / Nhóm | Khoảng bài | Tiến độ | Bảng theo dõi chi tiết |
| :--- | :---: | :---: | :--- |
| **Batch 1** | Problems 001 - 100 | 1 / 100 | [problems-from-1-to-100/README.md](./problems-from-1-to-100/README.md) |
| **Batch 2** | Problems 101 - 200 | 0 / 100 | *(Sẽ cập nhật khi hoàn thành Batch 1)* |
| **Batch 3** | Problems 201 - 300 | 0 / 100 | *(Sẽ cập nhật khi hoàn thành Batch 2)* |

---

## Quy Trình Luyện Tập Hàng Ngày

1. **Nhận bài và phân tích:** Đọc kỹ đề bài tại `README.md` của từng bài toán, xác định các trường hợp biên (edge cases) và ràng buộc dữ liệu.
2. **Thực thi trên LeetCode:** Viết mã trong `Solution.java` và nộp kiểm tra trực tiếp trên LeetCode.
3. **Vấn đáp kỹ thuật (Mock Interview):** Cố vấn AI sẽ đặt các câu hỏi phản biện về cấu trúc dữ liệu, trường hợp xấu nhất (worst-case) và trade-off giữa Time & Space.
4. **Đánh giá và chấm điểm:** Nhận bảng điểm theo chuẩn Big Tech (Thang điểm 10) và cập nhật bài học vào `explain.md`.

# 🚀 Daily Code Challenge (Java 17)

Chào mừng bạn đến với **Daily Code Challenge** — dự án cá nhân được xây dựng bởi **Đình** nhằm rèn luyện tư duy thuật toán, nâng cao năng lực giải quyết vấn đề và xây dựng thói quen lập trình kỷ luật mỗi ngày.

---

## 🎯 Mục Tiêu Dự Án

* **Rèn luyện phản xạ thuật toán:** Giải quyết đều đặn các bài toán từ LeetCode từ mức độ cơ bản đến nâng cao.
* **Tư duy phỏng vấn Big Tech:** Không chỉ giải bài để "pass test", mỗi giải pháp đều trải qua quá trình **vấn đáp và phản biện gắt gao** (Mock Interview) để bảo vệ tính tối ưu của thuật toán và cấu trúc dữ liệu.
* **Tài liệu hóa chuyên sâu:** Mỗi bài toán đều đi kèm một cẩm nang phân tích chi tiết (`explain.md`) bao gồm ý tưởng cốt lõi, diễn giải từng bước và phân tích độ phức tạp thời gian/không gian ($O(N)$ Big-O).
* **Code Java 17 chuẩn mực:** Áp dụng các cú pháp hiện đại của Java, chú trọng clean code, đặt tên rõ nghĩa và cấu trúc mạch lạc.

---

## 📂 Cấu Trúc Thư Mục

Dự án được phân loại theo từng nhóm 100 bài toán để tiện theo dõi streak và tiến độ:

```
daily-code-challenge/
├── README.md                           # Bảng điều khiển tiến độ và giới thiệu dự án
├── GEMINI.md                           # Bộ quy tắc cố vấn phỏng vấn kỹ thuật
├── .agents/skills/leetcode-interviewer # Skill Antigravity đóng vai Technical Interviewer
└── problems-from-1-to-100/
    ├── problem-01/
    │   ├── README.md                   # Đề bài toán, ràng buộc & ví dụ
    │   ├── Solution.java               # Code giải thuật bằng Java 17 (chuẩn LeetCode)
    │   └── explain.md                  # Cẩm nang phân tích chuyên sâu & đúc kết
    └── ...
```

---

## 📊 Bảng Theo Dõi Tiến Độ (Progress Tracker)

> **Thống kê:** Tổng số bài: **0** | 🟢 Easy: **0** | 🟡 Medium: **0** | 🔴 Hard: **0**

| # | Bài toán | Chủ đề / Pattern | Độ khó | Code | Phân tích chi tiết | Trạng thái |
| :-: | :--- | :--- | :-: | :-: | :-: | :-: |
| 01 | [Two Sum](https://leetcode.com/problems/two-sum/) | Arrays & Hashing | 🟢 Easy | [Solution.java](./problems-from-1-to-100/problem-01/Solution.java) | [explain.md](./problems-from-1-to-100/problem-01/explain.md) | 🔄 In Progress |

---

## 🛠️ Quy Trình Luyện Tập Hàng Ngày

1. **Nhận bài & Phân tích:** Đọc kỹ đề bài tại `README.md` của từng bài toán, xác định các trường hợp biên (edge cases) và ràng buộc dữ liệu.
2. **Thực thi trên LeetCode:** Viết mã trong `Solution.java` và nộp kiểm tra trực tiếp trên LeetCode.
3. **Vấn đáp kỹ thuật (Mock Interview):** Cố vấn AI sẽ đặt các câu hỏi phản biện về cấu trúc dữ liệu, trường hợp xấu nhất (worst-case) và trade-off giữa Time & Space.
4. **Đánh giá & Chấm điểm:** Nhận bảng điểm theo chuẩn Big Tech (Thang điểm 10) và cập nhật bài học vào `explain.md`.

# LeetCode 242: Valid Anagram

- **Liên kết bài toán:** [leetcode.com/problems/valid-anagram](https://leetcode.com/problems/valid-anagram/)
- **Độ khó:** Easy
- **Chủ đề:** Arrays & Hashing, String, Sorting

---

## 1. Yêu Cầu Đề Bài

Cho hai chuỗi ký tự `s` và `t`. Hãy trả về `true` nếu `t` là một **anagram** (chuỗi đảo chữ / hoán vị ký tự) của `s`, và `false` nếu ngược lại.

Một chuỗi được gọi là **Anagram** khi nó được tạo ra bằng cách sắp xếp lại các chữ cái của một chuỗi khác, trong đó sử dụng tất cả các ký tự gốc với số lần xuất hiện chính xác như ban đầu.

---

## 2. Ví Dụ

### Ví dụ 1:
```text
Input: s = "anagram", t = "nagaram"
Output: true
Giải thích: Cả hai chuỗi đều bao gồm: 3 ký tự 'a', 1 ký tự 'n', 1 ký tự 'g', 1 ký tự 'r', và 1 ký tự 'm'.
```

### Ví dụ 2:
```text
Input: s = "rat", t = "car"
Output: false
Giải thích: Chuỗi "rat" có ký tự 't', trong khi "car" không có 't' mà có 'c'.
```

---

## 3. Ràng Buộc (Constraints)

* $1 \le \text{s.length}, \text{t.length} \le 5 \times 10^4$
* `s` và `t` chỉ bao gồm các chữ cái tiếng Anh in thường (lowercase English letters).

---

## 4. Thử Thách Mở Rộng (Follow-up)

Nếu đầu vào chứa các ký tự **Unicode** (không chỉ gói gọn trong 26 chữ cái tiếng Anh từ `'a'` đến `'z'`), bạn sẽ điều chỉnh thuật toán và cấu trúc dữ liệu của mình như thế nào?


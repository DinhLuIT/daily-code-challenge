# LeetCode 01: Two Sum

- **Liên kết bài toán:** [leetcode.com/problems/two-sum](https://leetcode.com/problems/two-sum/)
- **Độ khó:** 🟢 Easy
- **Chủ đề:** Arrays, Hash Table

---

## 1. Yêu Cầu Đề Bài

Cho một mảng số nguyên `nums` và một số nguyên `target`. Hãy tìm và trả về **chỉ số (indices)** của hai số trong mảng sao cho tổng của chúng bằng `target`.

* Giả định rằng mỗi đầu vào luôn có **chính xác một cặp nghiệm duy nhất**.
* Bạn **không được sử dụng cùng một phần tử hai lần** (tức là không thể lấy một chỉ số 2 lần).
* Kết quả có thể trả về theo bất kỳ thứ tự nào.

---

## 2. Ví Dụ

### Ví dụ 1:
```text
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Giải thích: Vì nums[0] + nums[1] == 9, nên ta trả về [0, 1].
```

### Ví dụ 2:
```text
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]
```

### Ví dụ 3:
```text
Input: nums = [3, 3], target = 6
Output: [0, 1]
```

---

## 3. Ràng Buộc (Constraints)

* $2 \le \text{nums.length} \le 10^4$
* $-10^9 \le \text{nums}[i] \le 10^9$
* $-10^9 \le \text{target} \le 10^9$
* Luôn tồn tại **chính xác một** đáp án hợp lệ.

---

## 4. Thử Thách Mở Rộng (Follow-up)
Bạn có thể tìm ra thuật toán có độ phức tạp thời gian nhỏ hơn $O(n^2)$ không?

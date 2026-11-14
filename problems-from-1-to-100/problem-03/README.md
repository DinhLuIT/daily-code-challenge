# LeetCode 217: Contains Duplicate

- **Liên kết bài toán:** [leetcode.com/problems/contains-duplicate](https://leetcode.com/problems/contains-duplicate/)
- **Độ khó:** Easy
- **Chủ đề:** Arrays & Hashing, Hash Table, Sorting

---

## 1. Yêu Cầu Đề Bài

Cho một mảng số nguyên `nums`. Hãy trả về `true` nếu có bất kỳ giá trị nào xuất hiện ít nhất hai lần trong mảng, và trả về `false` nếu tất cả các phần tử trong mảng đều phân biệt (distinct).

---

## 2. Ví Dụ

### Ví dụ 1:
```text
Input: nums = [1,2,3,1]
Output: true
Giải thích: Phần tử 1 xuất hiện tại các chỉ số index 0 và 3.
```

### Ví dụ 2:
```text
Input: nums = [1,2,3,4]
Output: false
Giải thích: Tất cả các phần tử trong mảng đều phân biệt.
```

### Ví dụ 3:
```text
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
```

---

## 3. Ràng Buộc (Constraints)

* $1 \le \text{nums.length} \le 10^5$
* $-10^9 \le \text{nums}[i] \le 10^9$

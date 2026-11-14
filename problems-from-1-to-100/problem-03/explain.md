# LeetCode 217: Contains Duplicate

## 1. Mô tả bài toán

Cho một mảng số nguyên `nums`. Hãy xác định xem có bất kỳ phần tử nào xuất hiện ít nhất hai lần trong mảng hay không. Trả về `true` nếu có phần tử lặp lại, ngược lại trả về `false` nếu mọi phần tử trong mảng đều phân biệt (distinct).

### Ràng buộc kỹ thuật
- $1 \le \text{nums.length} \le 10^5$
- $-10^9 \le \text{nums}[i] \le 10^9$

---

## 2. Ý tưởng cốt lõi (Intuition)

### Cách tiếp cận 1: Vét cạn (Brute Force)
- **Ý tưởng:** Dùng 2 vòng lặp lồng nhau duyệt qua tất cả các cặp $(i, j)$ với $i \ne j$. Nếu `nums[i] == nums[j]`, kết luận có phần tử trùng lặp.
- **Độ phức tạp:** Thời gian $O(n^2)$, bộ nhớ $O(1)$.
- **Đánh giá:** Với $n = 10^5$, $n^2 = 10^{10}$ phép tính, giải pháp này chắc chắn bị Time Limit Exceeded (TLE) trên LeetCode.

### Cách tiếp cận 2: Sắp xếp tại chỗ (In-place Sorting) - Tối ưu Bộ nhớ
- **Ý tưởng:** Sắp xếp mảng `nums` theo thứ tự tăng dần bằng `Arrays.sort(nums)`. Sau khi sắp xếp, nếu có phần tử trùng nhau, chúng bắt buộc phải nằm liền kề. Ta chỉ cần duyệt một lượt kiểm tra nếu `nums[i] == nums[i - 1]`.
- **Độ phức tạp:** Thời gian $O(n \log n)$, bộ nhớ phụ $O(1)$ (hoặc $O(\log n)$ call stack của Dual-Pivot Quicksort trong Java).
- **Đánh đổi (Trade-off):**
  - Ưu điểm: Tiết kiệm tối đa bộ nhớ RAM, không phát sinh chi phí phân bổ đối tượng trên Heap.
  - Nhược điểm: Thay đổi mảng gốc (side-effect) và thời gian thực thi chậm hơn so với cách tiếp cận dùng bảng băm.

### Cách tiếp cận 3: Bảng băm / Tập hợp băm (HashSet) - Tối ưu Thời gian
- **Ý tưởng:** Duyệt mảng từ trái sang phải, dùng một cấu trúc `HashSet` để lưu các phần tử đã duyệt qua (`seen`). Với mỗi phần tử `number`:
  - Thêm `number` vào `HashSet`.
  - Nếu phương thức `set.add(number)` trả về `false` (nghĩa là phần tử đã tồn tại trong tập hợp), lập tức dừng thuật toán và trả về `true` (Early Exit).
  - Nếu duyệt hết mảng mà không phát hiện phần tử trùng lặp, trả về `false`.
- **Độ phức tạp:** Thời gian $O(n)$, bộ nhớ $O(n)$.
- **Ưu điểm vượt trội:** Đạt thời gian tuyến tính $O(n)$ tối ưu cho bài toán kiểm tra trùng lặp.

---

## 3. Giải thích thuật toán từng bước

Quy trình thực thi của thuật toán tối ưu dùng `HashSet`:

1. **Bước 1 (Tính toán dung lượng khởi tạo):**
   - Để tránh kích hoạt cơ chế `rehash` khi kích thước tập hợp tăng lên, ta khởi tạo `HashSet` với dung lượng được tính toán trước:
     $$\text{initialCapacity} = \left\lceil \frac{n}{0.75} \right\rceil + 1$$
   - Với Java 19 trở lên, có thể dùng `HashSet.newHashSet(nums.length)`. Trên Java 17, ta tính `(int) Math.ceil(nums.length / 0.75f)`.

2. **Bước 2 (Duyệt mảng và kiểm tra ngắt sớm):**
   - Sử dụng vòng lặp for-each duyệt từng phần tử `number` trong `nums`.
   - Gọi `seen.add(number)`. Hàm `add()` của `HashSet` trong Java trả về:
     - `true`: Nếu phần tử chưa từng có trong set và được thêm thành công.
     - `false`: Nếu phần tử đã tồn tại sẵn trong set.
   - Nếu kết quả là `false`, phát hiện phần tử lặp lại, lập tức trả về `true`.

3. **Bước 3 (Kết luận):**
   - Nếu duyệt hết toàn bộ mảng `nums` mà không có lần gọi `add()` nào trả về `false`, trả về `false`.

---

## 4. Phân tích độ phức tạp Big-O (Time & Space)

### Thời gian (Time Complexity)
- **Trung bình (Average Case):** $O(n)$
  - Mỗi thao tác tính mã băm và kiểm tra/thêm vào `HashSet` có độ phức tạp trung bình là $O(1)$.
  - Ta duyệt qua mảng tối đa $n$ lần. Tổng thời gian thực thi là $O(n)$.
- **Trường hợp xấu nhất (Worst Case):** $O(n \log n)$ trên Java 8+
  - Nếu xảy ra xung đột băm nghiêm trọng (Hash Collision) trên các bucket, Java 8+ chuyển đổi cấu trúc danh sách liên kết (LinkedList) của bucket thành Cây đỏ-đen (Red-Black Tree), do đó mỗi thao tác tra cứu/thêm tốn $O(\log k)$ thay vì bị suy biến thành $O(n)$ như các phiên bản Java trước đây.

### Không gian bộ nhớ (Space Complexity)
- **Độ phức tạp:** $O(n)$
  - Trong trường hợp xấu nhất (tất cả các phần tử trong mảng đều phân biệt), `HashSet` phải lưu trữ toàn bộ $n$ phần tử.

### Phân tích chuyên sâu JVM Internals & System Design

1. **Cơ chế Load Factor và Rehash trong `HashSet`:**
   - Bản chất `HashSet` là một lớp bọc bên ngoài của `HashMap` (`map.put(key, PRESENT) == null`).
   - Mặc định, hệ số tải `DEFAULT_LOAD_FACTOR` là `0.75f`. Ngưỡng kích hoạt mở rộng bảng băm (Rehash Threshold) được tính bằng:
     $$\text{threshold} = \text{capacity} \times \text{loadFactor}$$
   - Nếu truyền thẳng `nums.length` (ví dụ $10^5$) vào constructor, capacity thực tế được làm tròn lên lũy thừa của 2 là $131,072$. Tuy nhiên, ngưỡng threshold chỉ là:
     $$131,072 \times 0.75 = 98,304 < 100,000$$
   - Khi thêm đến phần tử thứ $98,305$, bảng băm sẽ bị kích hoạt rehash: cấp phát mảng bucket mới có kích thước gấp đôi ($262,144$) và di chuyển lại toàn bộ $98,304$ phần tử cũ, gây tụt giảm hiệu năng đột ngột.

2. **Chi phí Autoboxing và Phân bổ Heap:**
   - Mảng nguyên thủy `int[]` gồm $10^5$ phần tử chỉ chiếm khoảng:
     $$10^5 \times 4 \text{ bytes} \approx 400 \text{ KB}$$
   - Khi đưa vào `HashSet<Integer>`, mỗi phần tử `int` bị autobox thành một đối tượng `Integer` (16 bytes trên 64-bit JVM với Compressed OOPs).
   - Mỗi phần tử trong `HashMap` tạo thêm một đối tượng `Node<K, V>` (32 bytes).
   - Cộng thêm tham chiếu 4 bytes trong mảng bucket, mỗi phần tử ngốn ít nhất $52 \text{ bytes}$.
   - Tổng bộ nhớ cho $10^5$ phần tử phân biệt lên tới hơn $5.2 \text{ MB} - 8 \text{ MB}$ (gấp hơn 15 lần so với mảng nguyên thủy).

3. **Cơ chế Treeify trong Java (Hash Collision Resilience):**
   - Khi nhiều key có mã băm rơi vào cùng một bucket, Java lưu chúng dưới dạng LinkedList.
   - Khi số lượng node trong một bucket đạt ngưỡng `TREEIFY_THRESHOLD = 8` VÀ tổng dung lượng bảng băm đạt ít nhất `MIN_TREEIFY_CAPACITY = 64`, bucket đó sẽ tự động chuyển đổi từ danh sách liên kết thành cây đỏ-đen (`TreeNode`).
   - Khi kích thước bucket giảm xuống `UNTREEIFY_THRESHOLD = 6`, cây sẽ được chuyển ngược lại thành danh sách liên kết.

4. **Xử lý luồng dữ liệu lớn (Data Stream / Big Data):**
   - Khi dữ liệu là một stream khổng lồ gồm hàng tỉ số nguyên vượt quá dung lượng RAM, cấu trúc `HashSet` sẽ gây tràn bộ nhớ (`OutOfMemoryError`).
   - **Giải pháp xác suất (Probabilistic Data Structure):** Sử dụng **Bloom Filter**. Bloom Filter sử dụng một mảng bit nhỏ gọn cùng nhiều hàm băm độc lập để kiểm tra phần tử. Nó bảo đảm:
     - Nếu Bloom Filter báo phần tử chưa từng xuất hiện $\rightarrow$ Chắc chắn 100% chưa xuất hiện (No False Negatives).
     - Nếu báo phần tử đã xuất hiện $\rightarrow$ Có thể có một tỷ lệ nhỏ dương tính giả (False Positive Rate có thể cấu hình được, ví dụ 0.1%).
   - **Giải pháp chính xác tuyệt đối:** Sử dụng External Merge Sort hoặc kỹ thuật phân vùng băm (Hash Partitioning) chia nhỏ stream thành các file trên đĩa cứng rồi xử lý từng phân vùng.

---

## 5. Code hoàn chỉnh & Lưu ý tránh bẫy

### Giải pháp 1: HashSet tối ưu thời gian $O(n)$ (Khuyên dùng)

```java
package problems_from_1_to_100.problem_03;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Tinh toan initial capacity de ngan chan rehash: ceil(n / 0.75)
        int initialCapacity = (int) Math.ceil(nums.length / 0.75f);
        Set<Integer> seen = new HashSet<>(initialCapacity);

        for (int number : nums) {
            // Set.add tra ve false neu phan tu da ton tai trong set
            if (!seen.add(number)) {
                return true;
            }
        }

        return false;
    }
}
```

### Giải pháp 2: Sorting tối ưu bộ nhớ $O(1)$ auxiliary space

```java
package problems_from_1_to_100.problem_03;

import java.util.Arrays;

class SolutionSorting {
    public boolean containsDuplicate(int[] nums) {
        // Sap xep in-place: O(n log n) thoi gian, O(1) bo nho phu
        Arrays.sort(nums);

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i - 1]) {
                return true;
            }
        }

        return false;
    }
}
```

### Các bẫy thường gặp (Common Pitfalls)
1. **Gọi `contains()` rồi mới gọi `add()`:** Nhiều lập trình viên viết `if (seen.contains(x)) return true; else seen.add(x);`. Việc này khiến JVM phải băm và duyệt bucket hai lần cho cùng một phần tử. Tận dụng trực tiếp giá trị trả về của `seen.add(x)` giúp giảm một nửa số lần tra cứu.
2. **Không chú ý đến Load Factor:** Truyền trực tiếp `nums.length` vào constructor của `HashSet` mà không tính bù trừ theo hệ số tải `0.75` vẫn khiến bảng băm bị rehash và sao chép mảng ở những phần tử cuối.
3. **Đặt tên biến gây khó hiểu:** Đặt tên dạng phủ định lồng ghép như `unDuplicateNums` gây khó đọc và đi ngược lại quy chuẩn Clean Code. Nên dùng tên ngắn gọn, rõ nghĩa như `seen` hoặc `visited`.

# LeetCode 01: Two Sum

## 1. Mô tả bài toán

Cho một mảng số nguyên `nums` và một số nguyên `target`. Nhiệm vụ là tìm ra hai chỉ số (indices) $i$ và $j$ sao cho:
$$\text{nums}[i] + \text{nums}[j] = \text{target} \quad (i \ne j)$$

### Ràng buộc kỹ thuật
- $2 \le \text{nums.length} \le 10^4$
- $-10^9 \le \text{nums}[i] \le 10^9$
- $-10^9 \le \text{target} \le 10^9$
- Đề bài đảm bảo luôn tồn tại chính xác một cặp nghiệm hợp lệ.
- Không được dùng cùng một phần tử hai lần ($i \ne j$).

---

## 2. Ý tưởng cốt lõi (Intuition)

### Cách tiếp cận 1: Vét cạn (Brute Force)
- Ý tưởng: Dùng 2 vòng lặp lồng nhau duyệt qua mọi cặp chỉ số $(i, j)$ với $j > i$ để kiểm tra xem $\text{nums}[i] + \text{nums}[j] == \text{target}$.
- Nhược điểm: Với $N = 10^4$, số cặp cần kiểm tra là $\frac{N(N-1)}{2} \approx 5 \times 10^7$ phép so sánh. Độ phức tạp thời gian $O(n^2)$ là quá lớn và không đáp ứng được yêu cầu của hệ thống hiệu năng cao.

### Cách tiếp cận 2: Sắp xếp kết hợp Hai con trỏ (Sort + Two Pointers)
- Ý tưởng: Nếu mảng đã sắp xếp tăng dần, ta có thể đặt con trỏ `left = 0`, `right = n - 1` rồi co dần theo tổng `nums[left] + nums[right]`.
- Vấn đề gặp phải: Đề bài yêu cầu trả về **chỉ số ban đầu (original indices)**. Nếu sắp xếp trực tiếp mảng nguyên thủy `int[]`, toàn bộ vị trí ban đầu sẽ bị mất.
- Trade-off: Muốn giữ lại chỉ số ban đầu, ta buộc phải tạo một mảng phụ chứa các cặp `(giá trị, chỉ số ban đầu)` rồi mới sắp xếp. Việc này tốn thêm $O(n)$ không gian bộ nhớ và thời gian là $O(n \log n)$ do công đoạn sắp xếp. Do đó, phương pháp này kém tối ưu hơn Hash Table cả về mặt thời gian.

### Cách tiếp cận 3: Bảng băm một lần duyệt (One-Pass Hash Table) - Tối ưu nhất
- Biến đổi phương trình toán học: Thay vì tìm hai biến cùng lúc ($A + B = \text{target}$), ta cố định một biến và chuyển vế tìm biến còn lại:
  $$\text{complement} = \text{target} - \text{nums}[i]$$
- Sử dụng cấu trúc dữ liệu Hash Table (trong Java là `java.util.HashMap`) để lưu trữ ánh xạ:
  $$\text{Key: Giá trị phần tử } (\text{nums}[i]) \longrightarrow \text{Value: Chỉ số } (i)$$
- Khi đứng tại phần tử `nums[i]`, ta kiểm tra xem `complement` đã xuất hiện trong bảng băm trước đó hay chưa:
  - Nếu đã tồn tại: Cặp chỉ số cần tìm chính là `[map.get(complement), i]`.
  - Nếu chưa tồn tại: Đưa giá trị hiện tại `nums[i]` cùng chỉ số `i` vào bảng băm và tiếp tục duyệt.

---

## 3. Giải thích thuật toán từng bước

Quy trình xử lý của giải thuật One-Pass Hash Table:

1. **Khởi tạo:**
   - Tạo một bảng băm `map` ánh xạ từ giá trị phần tử (`Integer`) sang chỉ số tương ứng (`Integer`).

2. **Duyệt một lượt qua mảng (Single Loop from $i = 0$ đến $n - 1$):**
   - Tính toán phần bù cần tìm: `complement = target - nums[i]`.
   - Kiểm tra nhanh trong bảng băm: `map.containsKey(complement)`.
     - **Nếu tìm thấy:** Nghĩa là ta đã gặp một phần tử có giá trị đúng bằng `complement` tại chỉ số `map.get(complement)` trong quá khứ. Trả về ngay lập tức mảng kết quả `new int[]{map.get(complement), i}`.
     - **Nếu không tìm thấy:** Lưu phần tử hiện tại vào bảng băm bằng `map.put(nums[i], i)`. Việc này phục vụ cho việc tra cứu của các phần tử phía sau.

3. **Tính chất an toàn của One-Pass:**
   - Bằng cách chỉ đưa phần tử vào bảng băm *sau* khi kiểm tra `complement`, ta đảm bảo một phần tử không bao giờ tự bắt cặp với chính nó (tránh bẫy $i == j$).
   - Nếu có hai số trùng nhau tạo thành nghiệm (ví dụ `nums = [3, 3]`, `target = 6`), khi duyệt đến số 3 thứ hai ở chỉ số 1, số 3 đầu tiên ở chỉ số 0 đã nằm sẵn trong map. Thuật toán tìm thấy nghiệm ngay lập tức mà không bị ghi đè key.

---

## 4. Phân tích độ phức tạp Big-O (Time & Space)

### Thời gian (Time Complexity)
- **Trung bình (Average Case):** $O(n)$
  - Ta chỉ duyệt qua mảng đúng một lần ($n$ bước).
  - Thao tác tìm kiếm `containsKey()` và thêm `put()` trong `HashMap` có độ phức tạp trung bình là $O(1)$.
- **Xấu nhất (Worst Case):** $O(n)$ trên Java 8+
  - Nếu xảy ra xung đột hàm băm (hash collisions) cực kỳ nghiêm trọng, từ Java 8 trở đi, các phần tử trong cùng một bucket sẽ được chuyển hóa thành cây đỏ-đen (Red-Black Tree) khi vượt ngưỡng `TREEIFY_THRESHOLD = 8`.
  - Khi đó thời gian tìm kiếm trên một bucket là $O(\log k)$, thời gian toàn cục tồi nhất vẫn được khống chế ở $O(n \log k)$, vượt trội hoàn toàn so với $O(n)$ dạng danh sách liên kết của các phiên bản Java cũ.

### Không gian (Space Complexity)
- **Độ phức tạp:** $O(n)$
  - Trong trường hợp xấu nhất, bảng băm sẽ phải lưu trữ tối đa $n - 1$ phần tử trước khi tìm thấy cặp nghiệm ở phần tử cuối cùng.

### Phân tích chuyên sâu Java Internals & Bộ nhớ (Memory Footprint)
1. **Chi phí Autoboxing (`int` sang `Integer`):**
   - Một giá trị `int` nguyên thủy trong Java chỉ tốn đúng 4 bytes trên Stack hoặc Heap.
   - Khi đưa vào `HashMap<Integer, Integer>`, Java kích hoạt cơ chế autoboxing để bọc `int` thành đối tượng `Integer`.
   - Cấu trúc bộ nhớ của một `Integer` trên JVM 64-bit (bật Compressed OOPs):
     - Object Header: 12 bytes (8 bytes Mark Word + 4 bytes Klass Pointer).
     - Dữ liệu `int value`: 4 bytes.
     - Tổng cộng: 16 bytes per object (chưa kể 4 bytes con trỏ tham chiếu).
2. **Chi phí cấu trúc Node trong `HashMap`:**
   - Mỗi phần tử trong `HashMap` được lưu dưới dạng một đối tượng `Node<K, V>`:
     - Object Header: 12 bytes.
     - `int hash`: 4 bytes.
     - Tham chiếu `K key`: 4 bytes.
     - Tham chiếu `V value`: 4 bytes.
     - Tham chiếu `Node next`: 4 bytes.
     - Padding căn lề 8 bytes: 4 bytes.
     - Tổng: 32 bytes cho bản thân đối tượng Node.
   - Như vậy, tổng dung lượng để lưu một cặp `(int, int)` trong `HashMap` bao gồm: 32 bytes (Node) + 16 bytes (Key Integer) + 16 bytes (Value Integer) + tham chiếu mảng bucket = xấp xỉ 64 bytes, tốn gấp 16 lần so với 4 bytes của kiểu nguyên thủy.
3. **Tối ưu hóa Initial Capacity:**
   - Mặc định `HashMap` khởi tạo mảng bucket ban đầu với kích thước 16 và hệ số tải (load factor) là 0.75.
   - Khi số phần tử vượt ngưỡng `16 * 0.75 = 12`, `HashMap` sẽ kích hoạt `resize()` nhân đôi dung lượng mảng và thực hiện rehash toàn bộ các phần tử, gây tốn CPU.
   - Trong môi trường thực tế, nếu biết trước độ dài mảng $N$, ta có thể khởi tạo `new HashMap<>((int) Math.ceil(nums.length / 0.75f))` để tránh hoàn toàn chi phí rehash.

---

## 5. Code hoàn chỉnh & Lưu ý tránh bẫy

### Mã nguồn tối ưu (Java 17)

```java
package problems_from_1_to_100.problem_01;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        // Khởi tạo HashMap với kích thước ước lượng nhằm tránh chi phí rehash
        Map<Integer, Integer> numToIndex = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int complement = target - nums[i];

            // Kiểm tra xem phần bù đã xuất hiện ở các bước trước đó chưa
            if (numToIndex.containsKey(complement)) {
                return new int[]{numToIndex.get(complement), i};
            }

            // Lưu giá trị hiện tại cùng chỉ số vào bảng băm
            numToIndex.put(nums[i], i);
        }

        // Trường hợp không tìm thấy theo lý thuyết (mặc dù đề bài đảm bảo luôn có nghiệm)
        return new int[]{};
    }
}
```

### Các bẫy cần tránh (Pitfalls)
1. **Bẫy tràn số nguyên (Integer Overflow):**
   - Với ràng buộc $-10^9 \le \text{nums}[i] \le 10^9$, phép cộng trực tiếp `nums[i] + nums[j]` có thể đạt tới giá trị tuyệt đối $2 \times 10^9$.
   - Trong Java, kiểu `int` 32-bit có giới hạn từ $-2^{31} (-2,147,483,648)$ đến $2^{31} - 1 (2,147,483,647)$. Mặc dù $2 \times 10^9$ vẫn nằm trong giới hạn này, nó đã tiệm cận rất sát ngưỡng cực hạn.
   - Nếu đề bài mở rộng ràng buộc lên $2 \cdot 10^9$, biểu thức `nums[i] + nums[j]` sẽ lập tức bị tràn số và quay vòng thành số âm. Cách viết biến đổi thành phép trừ `complement = target - nums[i]` (hoặc ép sang `long`) là kỹ thuật thiết kế an toàn cần ghi nhớ.
2. **Bẫy trùng lặp phần tử (Duplicate Elements):**
   - Nếu áp dụng Two-Pass Hash Map (đưa toàn bộ mảng vào Map trước rồi mới duyệt tìm `complement`), khi gặp trường hợp mảng có các giá trị trùng nhau như `[3, 3]` với `target = 6`, giá trị put sau sẽ đè lên giá trị put trước, dẫn đến việc mất chỉ số ban đầu.
   - Kỹ thuật One-Pass Hash Map giải quyết triệt để vấn đề này vì khi đến phần tử trùng thứ hai, nghiệm đã được bắt cặp ngay lập tức với phần tử trùng thứ nhất đang có trong Map.

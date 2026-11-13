# LeetCode 242: Valid Anagram

## 1. Mô tả bài toán

Cho hai chuỗi ký tự `s` và `t`. Hãy xác định xem chuỗi `t` có phải là một **anagram** (chuỗi đảo chữ / hoán vị ký tự) của chuỗi `s` hay không. Trả về `true` nếu đúng, ngược lại trả về `false`.

Một chuỗi được định nghĩa là **Anagram** khi nó được tạo ra bằng cách sắp xếp lại các chữ cái của một chuỗi khác, trong đó sử dụng chính xác tất cả các ký tự gốc với số lần xuất hiện tương ứng.

### Ràng buộc kỹ thuật
- $1 \le \text{s.length}, \text{t.length} \le 5 \times 10^4$
- `s` và `t` chỉ bao gồm các chữ cái tiếng Anh in thường (`'a'` đến `'z'`).

### Câu hỏi mở rộng (Follow-up)
Nếu chuỗi đầu vào chứa các ký tự Unicode tùy ý, giải pháp sẽ cần được điều chỉnh như thế nào?

---

## 2. Ý tưởng cốt lõi (Intuition)

### Điều kiện tiên quyết: Kiểm tra độ dài chuỗi
Nếu `s.length() != t.length()`, hai chuỗi chắc chắn không thể là anagram của nhau. Đây là điều kiện biên (edge case) giúp ta loại trừ ngay lập tức với thời gian $O(1)$.

### Cách tiếp cận 1: Sắp xếp hai chuỗi (Sorting)
- **Ý tưởng:** Chuyển đổi cả hai chuỗi thành mảng ký tự `char[]`, sắp xếp mảng theo thứ tự bảng chữ cái bằng `Arrays.sort()`, sau đó so sánh xem hai mảng có bằng nhau hay không (`Arrays.equals()`).
- **Ưu điểm:** Cực kỳ ngắn gọn, dễ viết.
- **Nhược điểm:**
  - Độ phức tạp thời gian là $O(n \log n)$ do bước sắp xếp.
  - Tốn thêm $O(n)$ không gian bộ nhớ phụ để tạo các mảng ký tự `char[]` (do chuỗi `String` trong Java là immutable, không thể sắp xếp in-place).
  - Chưa đạt hiệu năng tối ưu cho các bài toán xử lý chuỗi lớn.

### Cách tiếp cận 2: Sử dụng Bảng băm (HashMap)
- **Ý tưởng:** Dùng một bảng băm `Map<Character, Integer>` để đếm số lần xuất hiện của từng ký tự trong chuỗi `s`, sau đó duyệt chuỗi `t` để trừ dần tần suất.
- **Ưu điểm:** Khái quát hóa tốt, có thể mở rộng tự nhiên cho toàn bộ bảng ký tự Unicode rộng lớn.
- **Nhược điểm trên dữ liệu giới hạn (`'a'` - `'z'`):**
  - **Overhead bộ nhớ lớn:** Java kích hoạt cơ chế autoboxing để bọc kiểu nguyên thủy `char` thành `Character` và `int` thành `Integer`. Mỗi đối tượng wrapper này tiêu tốn 16 bytes trên Heap (với JVM 64-bit).
  - Mỗi phần tử trong `HashMap` tốn thêm một đối tượng `Node<K, V>` (xấp xỉ 32 bytes).
  - Phân tán bộ nhớ trên Heap dẫn đến tỉ lệ cache miss cao ở CPU L1/L2 Cache.

### Cách tiếp cận 3: Bảng đếm tần suất cố định (Fixed-size Frequency Array) - Tối ưu nhất
- **Ý tưởng:** Do đề bài đảm bảo chuỗi chỉ chứa 26 chữ cái tiếng Anh in thường, ta có thể thay thế hoàn toàn bảng băm bằng một mảng nguyên thủy cố định `int[26]`.
- **Cơ chế băm trực tiếp (Direct Addressing):** Ký tự `c` được ánh xạ thẳng vào chỉ số mảng thông qua phép toán đơn giản:
  $$\text{index} = c - \text{'a'}$$
  Trong đó: `'a' - 'a' = 0`, `'b' - 'a' = 1`, ..., `'z' - 'a' = 25`.
- **Tối ưu hóa ngắt sớm (Early Termination):**
  1. Duyệt chuỗi `s` để đếm và tăng tần suất tương ứng trong `count[26]`.
  2. Duyệt chuỗi `t` để giảm tần suất `count[t.charAt(i) - 'a']--`.
  3. Nếu tại bất kỳ thời điểm nào giá trị tần suất bị giảm xuống dưới 0 (`count[...] < 0`), điều đó có nghĩa chuỗi `t` chứa một ký tự xuất hiện nhiều lần hơn chuỗi `s` (hoặc một ký tự không hề có trong `s`). Ta có thể lập tức trả về `false` mà không cần duyệt hết chuỗi.
  4. Vì hai chuỗi có cùng độ dài, nếu không có bất kỳ ký tự nào bị âm thì chắc chắn tất cả các phần tử trong mảng đều bằng đúng 0, kết luận hai chuỗi là anagram.

---

## 3. Giải thích thuật toán từng bước

Quy trình thực thi của thuật toán Frequency Array:

1. **Bước 1 (Kiểm tra độ dài):**
   - So sánh `s.length()` và `t.length()`. Nếu khác nhau, trả về `false` ngay lập tức.

2. **Bước 2 (Khởi tạo mảng đếm):**
   - Khởi tạo mảng số nguyên `int[] count = new int[26]`. Mặc định trong Java, các phần tử của mảng `int` được gán giá trị 0.

3. **Bước 3 (Ghi nhận tần suất từ chuỗi s):**
   - Lặp qua từng chỉ số $i$ từ $0$ đến $n - 1$:
     - Lấy ký tự `s.charAt(i)`.
     - Tăng phần tử tại vị trí `s.charAt(i) - 'a'` lên 1 đơn vị.

4. **Bước 4 (Khấu trừ và kiểm tra ngắt sớm với chuỗi t):**
   - Lặp qua từng chỉ số $i$ từ $0$ đến $n - 1$:
     - Xác định vị trí `idx = t.charAt(i) - 'a'`.
     - Giảm giá trị `count[idx]--`.
     - Kiểm tra điều kiện: Nếu `count[idx] < 0`, lập tức trả về `false`.

5. **Bước 5 (Kết luận):**
   - Nếu duyệt hết chuỗi `t` mà không vi phạm điều kiện âm, trả về `true`.

---

## 4. Phân tích độ phức tạp Big-O (Time & Space)

### Thời gian (Time Complexity)
- **Độ phức tạp:** $O(n)$
  - Trong đó $n$ là độ dài của chuỗi `s` (và `t`).
  - Ta duyệt qua chuỗi `s` một lần ($n$ phép toán) và chuỗi `t` tối đa một lần ($n$ phép toán).
  - Mọi thao tác truy xuất mảng bằng chỉ số `count[idx]` đều có chi phí $O(1)$ tuyệt đối.
  - Tổng thời gian thực thi là $O(n + n) = O(n)$.

### Không gian bộ nhớ (Space Complexity)
- **Độ phức tạp:** $O(1)$
  - Mảng `count` có kích thước cố định là 26 phần tử số nguyên `int`, hoàn toàn độc lập với độ dài $n$ của chuỗi đầu vào ($1 \le n \le 5 \times 10^4$).
  - Dung lượng mảng `int[26]` trên JVM chỉ xấp xỉ 120 bytes, đáp ứng tiêu chuẩn $O(1)$ auxiliary space.

### Phân tích chuyên sâu JVM Internals & CPU Cache Locality
1. **CPU Cache Locality:**
   - Mảng `int[26]` được cấp phát dưới dạng một khối ô nhớ liên tục trên Heap. Toàn bộ mảng nằm gọn trong một Cache Line (thường là 64 bytes) của CPU L1 Data Cache.
   - Khi CPU nạp một phần tử của mảng vào cache, các phần tử lân cận cũng được nạp đồng thời, mang lại tốc độ truy xuất cực nhanh với độ trễ chỉ khoảng 1 ns (L1 Cache hit).
   - Ngược lại, đối với `HashMap`, các đối tượng `Node` nằm rải rác trên Heap. Mỗi lần truy xuất qua con trỏ tham chiếu (pointer chasing) dễ gây ra L1/L2 Cache Miss, buộc CPU phải truy cập vào RAM chính với độ trễ cao hơn gấp hàng chục lần.

2. **Chi phí Autoboxing:**
   - Trong `HashMap<Character, Integer>`, việc chuyển đổi qua lại giữa `char` sang `Character` và `int` sang `Integer` liên tục tạo ra các đối tượng tạm thời trên Heap, làm gia tăng áp lực lên Garbage Collector (GC).
   - Sử dụng mảng nguyên thủy `int[]` loại bỏ hoàn toàn chi phí autoboxing và không tạo rác cho GC.

3. **Mở rộng bài toán với Unicode (Follow-up Question):**
   - Chuẩn Unicode hiện đại chứa hơn 149.000 ký tự với các mã code point trải dài từ `0x0000` đến `0x10FFFF`.
   - Nếu dữ liệu đầu vào chứa Unicode:
     - Mảng `int[26]` không thể sử dụng. Ta nên chuyển sang dùng `HashMap<Integer, Integer>` trong đó Key là Unicode Code Point (kiểu `int`), Value là tần suất xuất hiện.
     - Trong Java, kiểu `char` chỉ có độ rộng 16-bit (UTF-16 code unit). Những ký tự nằm ngoài Basic Multilingual Plane (BMP) như emoji hoặc chữ tượng hình hiếm có giá trị lớn hơn `0xFFFF` và được biểu diễn bằng một cặp 2 `char` gọi là **Surrogate Pairs**.
     - Nếu dùng `s.charAt(i)`, một ký tự 4-byte sẽ bị xẻ đôi thành hai mã `char` không hợp lệ.
     - Để xử lý Unicode an toàn, ta cần duyệt chuỗi thông qua stream code points: `s.codePoints()` hoặc dùng phương thức `s.codePointAt(i)` kết hợp dịch con trỏ bằng `Character.charCount(codePoint)`.

---

## 5. Code hoàn chỉnh & Lưu ý tránh bẫy

### Mã nguồn tối ưu (Java 17) - Fixed-size Frequency Array

```java
package problems_from_1_to_100.problem_02;

class Solution {
    public boolean isAnagram(String s, String t) {
        // Kiem tra dieu kien tien quyet: neu khac do dai, khong the la anagram
        if (s.length() != t.length()) {
            return false;
        }

        // Mang dem tan suat cho 26 chu cai tieng Anh in thuong ('a' den 'z')
        int[] count = new int[26];

        // Dem so lan xuat hien cua tung ky tu trong chuoi s
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // Giam tan suat theo chuoi t va kiem tra dieu kien ngat som
        for (int i = 0; i < t.length(); i++) {
            int idx = t.charAt(i) - 'a';
            count[idx]--;
            // Neu gia tri am, t chua ky tu khong co trong s hoac xuat hien nhieu lan hon
            if (count[idx] < 0) {
                return false;
            }
        }

        return true;
    }
}
```

### Các bẫy thường gặp (Common Pitfalls)
1. **Quên kiểm tra độ dài chuỗi ban đầu:** Bỏ qua `if (s.length() != t.length())` khiến thuật toán phải thực hiện hết vòng lặp hoặc dẫn đến kết quả sai lệch nếu chỉ duyệt theo chiều một chuỗi.
2. **Lạm dụng sắp xếp (`Arrays.sort`):** Dù code ngắn gọn hơn nhưng đẩy độ phức tạp thời gian từ $O(n)$ lên $O(n \log n)$ và tốn thêm $O(n)$ bộ nhớ do phải sao chép chuỗi sang mảng ký tự `toCharArray()`.
3. **Lạm dụng `HashMap` khi bảng chữ cái đã được cố định:** Khi đề bài đã giới hạn miền ký tự (ví dụ lowercase letters), dùng bảng băm là dấu hiệu của việc thiếu nhạy bén với ràng buộc dữ liệu và chưa tối ưu hóa hiệu năng hệ thống.

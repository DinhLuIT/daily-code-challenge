package problems_from_1_to_100.problem_02;

class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }

        int[] count = new int[26];

        // Đếm tần suất xuất hiện của từng ký tự trong chuỗi s
        for (int i = 0; i < s.length(); i++) {
            count[s.charAt(i) - 'a']++;
        }

        // Giảm tần suất theo chuỗi t, nếu có ký tự âm nghĩa là t có ký tự dư thừa
        for (int i = 0; i < t.length(); i++) {
            int idx = t.charAt(i) - 'a';
            count[idx]--;
            if (count[idx] < 0) {
                return false;
            }
        }

        return true;
    }
}

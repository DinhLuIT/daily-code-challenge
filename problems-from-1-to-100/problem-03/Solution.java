package problems_from_1_to_100.problem_03;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        // Tinh toan initial capacity de tranh rehash: ceil(n / 0.75)
        int initialCapacity = (int) Math.ceil(nums.length / 0.75f);
        Set<Integer> seen = new HashSet<>(initialCapacity);

        for (int number : nums) {
            // Set.add() tra ve false neu phan tu da ton tai trong set
            if (!seen.add(number)) {
                return true;
            }
        }

        return false;
    }
}

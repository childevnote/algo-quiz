import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(int[] nums) {
        int pick = nums.length / 2;
        Set<Integer> kinds = new HashSet<>();
        for (int n : nums) {
            kinds.add(n);
        }
        return Math.min(pick, kinds.size());
    }
}

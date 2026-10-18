import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] solution(int[] prices) {
        int n = prices.length;
        int[] ans = new int[n];
        Deque<Integer> stack = new ArrayDeque<>(); // ① 가격이 아직 떨어지지 않은 인덱스들을 보관 (비내림차순 스택)

        for (int i = 0; i < n; i++) {
            // ② 스택 꼭대기의 가격보다 현재 가격이 낮으면 → 그 가격의 유지 기간 확정
            while (!stack.isEmpty() && prices[stack.peek()] > prices[i]) {
                int j = stack.pop();
                ans[j] = i - j;
            }
            stack.push(i); // ③ 현재 인덱스를 스택에 남겨 둠
        }

        // ④ 스택에 남은 인덱스는 끝까지 가격이 떨어지지 않았으므로 남은 길이로 채움
        while (!stack.isEmpty()) {
            int j = stack.pop();
            ans[j] = n - 1 - j;
        }

        return ans;
    }
}

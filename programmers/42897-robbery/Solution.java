class Solution {
    public int solution(int[] money) {
        // 첫 집을 털면 마지막 집을 털 수 없고, 마지막 집을 털면 첫 집을 털 수 없다.
        // 원형을 두 개의 직선 구간으로 나눠 각각의 최댓값 중 큰 쪽을 택한다.
        return Math.max(rob(money, 0, money.length - 2),
                        rob(money, 1, money.length - 1));
    }

    private int rob(int[] money, int start, int end) {
        int prev2 = 0; // 두 집 전까지 턴 최대 금액
        int prev1 = 0; // 바로 전 집까지 턴 최대 금액
        for (int i = start; i <= end; i++) {
            int cur = Math.max(prev1, prev2 + money[i]);
            prev2 = prev1;
            prev1 = cur;
        }
        return prev1;
    }
}

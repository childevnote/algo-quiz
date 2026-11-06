import java.util.Arrays;

class Solution {
    public int solution(int[][] triangle) {
        // 1. 마지막 행을 누적 최대합 배열로 복사해 시작점으로 삼는다
        int[] dp = Arrays.copyOf(triangle[triangle.length - 1], triangle[triangle.length - 1].length);
        // 2. 아래 행부터 위로 올라가며 각 칸에 도달 가능한 최대합을 누적한다
        for (int i = triangle.length - 2; i >= 0; i--) {
            for (int j = 0; j < triangle[i].length; j++) {
                // 3. 바로 아래 두 칸 중 더 큰 쪽과 현재 값을 더한다
                dp[j] = triangle[i][j] + Math.max(dp[j], dp[j + 1]);
            }
        }
        // 4. 꼭대기에 남은 값이 전체 경로의 최대합이다
        return dp[0];
    }
}

// https://school.programmers.co.kr/learn/courses/30/lessons/42898
// 등굣길 (Lv.3, DP) — 2026-11-07

class Solution {
    public int solution(int m, int n, int[][] puddles) {
        final int MOD = 1_000_000_007;
        // puddles 좌표는 [x, y] (x: 열 1..m, y: 행 1..n)
        boolean[][] isPuddle = new boolean[n + 1][m + 1];
        for (int[] p : puddles) {
            isPuddle[p[1]][p[0]] = true;
        }
        // dp[y][x]: (1, 1)에서 (x, y)까지 도달하는 최단 경로 수
        int[][] dp = new int[n + 1][m + 1];
        dp[1][1] = 1;
        for (int y = 1; y <= n; y++) {
            for (int x = 1; x <= m; x++) {
                if (isPuddle[y][x]) {
                    dp[y][x] = 0;
                    continue;
                }
                if (x == 1 && y == 1) {
                    continue;
                }
                // 오른쪽·아래쪽 이동만 가능하므로, 위쪽과 왼쪽에서 오는 경우의 합
                dp[y][x] = (int) (((long) dp[y - 1][x] + dp[y][x - 1]) % MOD);
            }
        }
        return dp[n][m];
    }
}

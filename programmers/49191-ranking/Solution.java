class Solution {
    public int solution(int n, int[][] results) {
        // 1. 승패 관계 행렬: win[i][j] = i번 선수가 j번 선수를 이김 (0-indexed)
        boolean[][] win = new boolean[n][n];
        for (int[] r : results) {
            win[r[0] - 1][r[1] - 1] = true;
        }

        // 2. 플로이드-워셜로 승패 관계의 전이적 폐쇄 계산
        //    i가 k를 이기고 k가 j를 이기면 i는 j를 이긴다
        for (int k = 0; k < n; k++) {
            for (int i = 0; i < n; i++) {
                if (win[i][k]) {
                    for (int j = 0; j < n; j++) {
                        if (win[k][j]) {
                            win[i][j] = true;
                        }
                    }
                }
            }
        }

        // 3. 다른 모든 선수와 승패가 확정된 선수 카운트
        int answer = 0;
        for (int i = 0; i < n; i++) {
            int count = 0;
            for (int j = 0; j < n; j++) {
                if (i != j && (win[i][j] || win[j][i])) {
                    count++;
                }
            }
            if (count == n - 1) {
                answer++;
            }
        }
        return answer;
    }
}

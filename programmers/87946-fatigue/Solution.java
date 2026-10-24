// 피로도
// 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
// 풀이 날짜: 2026-10-23 (자동 풀이)

class Solution {
    private int answer = 0;
    private boolean[] visited;
    private int[][] dungeons;

    public int solution(int k, int[][] dungeons) {
        this.dungeons = dungeons;
        this.visited = new boolean[dungeons.length];
        backtrack(k, 0);
        return answer;
    }

    private void backtrack(int fatigue, int count) {
        // ① 현재까지 탐험한 던전 수로 정답 후보 갱신
        answer = Math.max(answer, count);
        // ② 남은 던전 중 입장 조건(최소 필요 피로도)을 만족하는 것을
        //    전부 시도하고, 복귀 시 방문 상태를 되돌린다 (백트래킹)
        for (int i = 0; i < dungeons.length; i++) {
            int req = dungeons[i][0], cost = dungeons[i][1];
            if (!visited[i] && fatigue >= req) {
                visited[i] = true;
                backtrack(fatigue - cost, count + 1);
                visited[i] = false;
            }
        }
    }
}

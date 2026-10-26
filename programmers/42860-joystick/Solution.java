class Solution {
    public int solution(String name) {
        // 1. 상하 조작: 각 자리마다 A에서 목표 문자까지 위/아래 중 짧은 쪽
        int answer = 0;
        for (int i = 0; i < name.length(); i++) {
            int up = name.charAt(i) - 'A';
            answer += Math.min(up, 26 - up);
        }

        // 2. 좌우 이동: 기본은 오른쪽으로 끝까지 가는 n-1회.
        //    연속된 'A' 구간을 만나면 되돌아가거나 왼쪽으로 먼저 돌아
        //    그 구간을 건너뛰는 편이 짧아질 수 있어 두 방향 모두 계산한다.
        int n = name.length();
        int move = n - 1;
        for (int i = 0; i < n; i++) {
            int nxt = i + 1;
            while (nxt < n && name.charAt(nxt) == 'A') {
                nxt++;
            }
            move = Math.min(move, i * 2 + n - nxt);
            move = Math.min(move, (n - nxt) * 2 + i);
        }
        return answer + move;
    }
}

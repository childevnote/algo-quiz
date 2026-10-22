// 카펫
// 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42842
// 풀이 날짜: 2026-10-22 (자동 풀이)

class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        // 노란 영역은 안쪽 직사각형 (가로 w, 세로 h)
        // 전체 가로 = w+2, 세로 = h+2 (테두리 갈색 1줄씩)
        for (int h = 1; h <= Math.sqrt(yellow); h++) {
            if (yellow % h == 0) {
                int w = yellow / h; // ① 노란 영역의 약수쌍 = 가능한 내부 가로/세로
                if ((w + 2) * (h + 2) == brown + yellow) { // ② 전체 격자 수와 일치하는 쌍 채택
                    answer[0] = w + 2;
                    answer[1] = h + 2;
                    break;
                }
            }
        }
        return answer;
    }
}

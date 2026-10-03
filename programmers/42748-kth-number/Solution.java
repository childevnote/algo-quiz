import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int t = 0; t < commands.length; t++) {
            int i = commands[t][0];
            int j = commands[t][1];
            int k = commands[t][2];
            // 1. 1-based 구간 [i, j]를 0-based로 복사 (copyOfRange의 끝은 exclusive)
            int[] sliced = Arrays.copyOfRange(array, i - 1, j);
            // 2. 복사본을 정렬 (원본 훼손 없음)
            Arrays.sort(sliced);
            // 3. k번째 수 (1-based → 0-based)
            answer[t] = sliced[k - 1];
        }
        return answer;
    }
}

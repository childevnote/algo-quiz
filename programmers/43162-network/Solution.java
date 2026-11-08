import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int solution(int n, int[][] computers) {
        // 1. 방문 여부를 기록할 배열
        boolean[] visited = new boolean[n];
        // 2. 네트워크 개수
        int count = 0;

        // 3. 아직 방문하지 않은 컴퓨터가 있으면 새 네트워크 시작
        for (int start = 0; start < n; start++) {
            if (visited[start]) continue;
            count++;
            // 4. 스택 기반 DFS로 연결된 컴퓨터를 모두 방문
            Deque<Integer> stack = new ArrayDeque<>();
            stack.push(start);
            visited[start] = true;
            while (!stack.isEmpty()) {
                int node = stack.pop();
                for (int nxt = 0; nxt < n; nxt++) {
                    if (computers[node][nxt] == 1 && !visited[nxt]) {
                        visited[nxt] = true;
                        stack.push(nxt);
                    }
                }
            }
        }
        return count;
    }
}

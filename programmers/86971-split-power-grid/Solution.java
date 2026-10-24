import java.util.*;

class Solution {
    public int solution(int n, int[][] wires) {
        // 1. 인접 리스트 구성 (노드 번호 1..n)
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) graph.add(new ArrayList<>());
        for (int[] w : wires) {
            graph.get(w[0]).add(w[1]);
            graph.get(w[1]).add(w[0]);
        }

        // 2. 1번 노드를 루트로 하는 반복 DFS로 부모·방문 순서 기록
        int[] parent = new int[n + 1];
        List<Integer> order = new ArrayList<>();
        Deque<Integer> stack = new ArrayDeque<>();
        stack.push(1);
        parent[1] = -1;
        while (!stack.isEmpty()) {
            int node = stack.pop();
            order.add(node);
            for (int nxt : graph.get(node)) {
                if (nxt != parent[node] && parent[nxt] == 0) {
                    parent[nxt] = node;
                    stack.push(nxt);
                }
            }
        }

        // 3. 역순으로 서브트리 크기 누적 (자식 크기를 부모에 합산)
        int[] size = new int[n + 1];
        Arrays.fill(size, 1);
        for (int i = order.size() - 1; i >= 0; i--) {
            int node = order.get(i);
            if (parent[node] > 0) size[parent[node]] += size[node];
        }

        // 4. 각 간선(부모-자식)을 끊었을 때 차이 = |n - 2 * 서브트리 크기|
        int answer = n;
        for (int node = 2; node <= n; node++) {
            answer = Math.min(answer, Math.abs(n - 2 * size[node]));
        }
        return answer;
    }
}

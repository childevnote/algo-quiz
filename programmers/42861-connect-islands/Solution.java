import java.util.Arrays;

class Solution {
    private int[] parent;

    private int find(int x) { // 3. 경로 압축을 적용한 find
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    public int solution(int n, int[][] costs) {
        // 1. 간선을 비용 오름차순으로 정렬
        Arrays.sort(costs, (a, b) -> Integer.compare(a[2], b[2]));

        parent = new int[n]; // 2. 각 섬의 집합 대표 (자기 자신으로 초기화)
        for (int i = 0; i < n; i++) {
            parent[i] = i;
        }

        int total = 0;
        int used = 0;
        for (int[] edge : costs) {
            int ra = find(edge[0]);
            int rb = find(edge[1]);
            // 4. 두 섬이 다른 집합이면 간선 선택 (사이클 방지)
            if (ra != rb) {
                parent[rb] = ra;
                total += edge[2];
                used++;
                // 5. n-1개 간선을 고르면 최소 신장 트리 완성
                if (used == n - 1) {
                    break;
                }
            }
        }
        return total;
    }
}

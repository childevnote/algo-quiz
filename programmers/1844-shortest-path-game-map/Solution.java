import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int[][] maps) {
        int n = maps.length;
        int m = maps[0].length;
        // 1. 방문 거리 배열: -1은 미방문, 시작 칸(0, 0)은 지나간 칸 1개로 초기화
        int[][] dist = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i][j] = -1;
            }
        }
        dist[0][0] = 1;
        // 2. BFS 큐: 시작 위치에서 출발
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{0, 0});
        // 3. 네 방향 이동
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0], y = cur[1];
            // 4. 목표 칸에 도달하면 그 즉시 거리가 최단 거리
            if (x == n - 1 && y == m - 1) {
                return dist[x][y];
            }
            for (int[] d : directions) {
                int nx = x + d[0], ny = y + d[1];
                // 5. 맵 안쪽, 벽이 아니고, 아직 방문하지 않은 칸만 이동
                if (nx >= 0 && nx < n && ny >= 0 && ny < m
                        && maps[nx][ny] == 1 && dist[nx][ny] == -1) {
                    dist[nx][ny] = dist[x][y] + 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }

        // 6. 큐가 비도록 목표 칸에 도달하지 못하면 -1
        return -1;
    }
}

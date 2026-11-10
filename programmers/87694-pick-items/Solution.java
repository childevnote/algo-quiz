import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        final int SIZE = 102;
        int[][] board = new int[SIZE][SIZE];

        // 1. 각 직사각형의 테두리를 보드에 표시한다 (좌표 2배 스케일).
        for (int[] r : rectangle) {
            int x1 = r[0] * 2, y1 = r[1] * 2, x2 = r[2] * 2, y2 = r[3] * 2;
            for (int x = x1; x <= x2; x++) {
                for (int y = y1; y <= y2; y++) {
                    if (x == x1 || x == x2 || y == y1 || y == y2) {
                        board[y][x] = 1;
                    }
                }
            }
        }

        // 2. 각 직사각형의 내부를 지운다. 겹친 직사각형의 내부에 들어간
        //    다른 직사각형의 테두리 조각도 함께 지워져 테두리만 남는다.
        for (int[] r : rectangle) {
            int x1 = r[0] * 2, y1 = r[1] * 2, x2 = r[2] * 2, y2 = r[3] * 2;
            for (int x = x1 + 1; x < x2; x++) {
                for (int y = y1 + 1; y < y2; y++) {
                    board[y][x] = 0;
                }
            }
        }

        // 3. BFS로 테두리를 따라 최단 경로를 탐색한다.
        int sx = characterX * 2, sy = characterY * 2;
        int tx = itemX * 2, ty = itemY * 2;
        int[][] dist = new int[SIZE][SIZE];
        for (int i = 0; i < SIZE; i++) {
            for (int j = 0; j < SIZE; j++) dist[i][j] = -1;
        }
        dist[sy][sx] = 0;
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[]{sx, sy});
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0], y = cur[1];
            // 4. 아이템에 도달하면 스케일된 거리를 2로 나눠 실제 거리를 반환한다.
            if (x == tx && y == ty) return dist[y][x] / 2;
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d], ny = y + dy[d];
                if (nx >= 0 && nx < SIZE && ny >= 0 && ny < SIZE
                        && board[ny][nx] == 1 && dist[ny][nx] == -1) {
                    dist[ny][nx] = dist[y][x] + 1;
                    queue.offer(new int[]{nx, ny});
                }
            }
        }
        return -1;
    }
}

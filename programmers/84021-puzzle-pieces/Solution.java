import java.util.*;

class Solution {
    public int solution(int[][] game_board, int[][] table) {
        int n = game_board.length;
        // 1. 게임 보드의 빈칸(0)들을 연결 요소(구멍)로 추출한다.
        List<List<int[]>> holes = extract(game_board, 0, n);
        // 2. 테이블의 조각(1)들을 연결 요소로 추출한다.
        List<List<int[]>> pieces = extract(table, 1, n);
        // 3. 각 구멍마다 회전시켜 모양이 일치하는 미사용 조각을 찾아 채운다.
        boolean[] used = new boolean[pieces.size()];
        int answer = 0;
        for (List<int[]> hole : holes) {
            Set<String> holeShape = normalize(hole);
            for (int i = 0; i < pieces.size(); i++) {
                if (used[i] || pieces.get(i).size() != hole.size()) continue;
                if (rotations(pieces.get(i)).contains(holeShape)) {
                    used[i] = true;
                    answer += hole.size();
                    break;
                }
            }
        }
        return answer;
    }

    // BFS로 target 값이 상하좌우로 연결된 칸들을 한 요소로 모은다.
    private List<List<int[]>> extract(int[][] board, int target, int n) {
        boolean[][] visited = new boolean[n][n];
        List<List<int[]>> components = new ArrayList<>();
        int[] dr = {1, -1, 0, 0};
        int[] dc = {0, 0, 1, -1};
        for (int r = 0; r < n; r++) {
            for (int c = 0; c < n; c++) {
                if (board[r][c] != target || visited[r][c]) continue;
                List<int[]> comp = new ArrayList<>();
                Queue<int[]> q = new ArrayDeque<>();
                q.offer(new int[]{r, c});
                visited[r][c] = true;
                while (!q.isEmpty()) {
                    int[] cur = q.poll();
                    comp.add(cur);
                    for (int d = 0; d < 4; d++) {
                        int nr = cur[0] + dr[d];
                        int nc = cur[1] + dc[d];
                        if (nr >= 0 && nr < n && nc >= 0 && nc < n
                                && !visited[nr][nc] && board[nr][nc] == target) {
                            visited[nr][nc] = true;
                            q.offer(new int[]{nr, nc});
                        }
                    }
                }
                components.add(comp);
            }
        }
        return components;
    }

    // 가장 위·왼쪽 칸을 (0, 0)으로 옮겨 위치와 무관한 모양만 남긴다.
    private Set<String> normalize(List<int[]> cells) {
        int minR = Integer.MAX_VALUE, minC = Integer.MAX_VALUE;
        for (int[] cell : cells) {
            minR = Math.min(minR, cell[0]);
            minC = Math.min(minC, cell[1]);
        }
        Set<String> shape = new HashSet<>();
        for (int[] cell : cells) {
            shape.add((cell[0] - minR) + "," + (cell[1] - minC));
        }
        return shape;
    }

    // 뒤집기는 금지, 90도씩 네 번 회전한 정규화 모양을 모두 만든다.
    private Set<Set<String>> rotations(List<int[]> cells) {
        Set<Set<String>> shapes = new HashSet<>();
        List<int[]> cur = new ArrayList<>(cells);
        for (int k = 0; k < 4; k++) {
            shapes.add(normalize(cur));
            List<int[]> next = new ArrayList<>();
            for (int[] cell : cur) {
                next.add(new int[]{cell[1], -cell[0]});
            }
            cur = next;
        }
        return shapes;
    }
}

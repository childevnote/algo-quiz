# 퍼즐 조각 채우기

- 문제: [퍼즐 조각 채우기](https://school.programmers.co.kr/learn/courses/30/lessons/84021)
- 레벨: Lv.3
- 카테고리: DFS/BFS
- 날짜: 2026-11-12

## 문제 핵심 요약

`game_board`의 빈칸(0)에 `table` 위에 놓인 퍼즐 조각(1)을 채워 넣는다. 조각은 한 번에 하나씩, 회전은 가능하지만 뒤집기는 불가능하다. 규칙에 맞게 최대한 많은 조각을 채웠을 때 총 몇 칸을 채울 수 있는지 구한다.

핵심 제한사항:

- 게임 보드와 테이블은 한 변이 3 이상 50 이하인 정사각 격자이다.
- 게임 보드의 0은 빈칸, 1은 이미 채워진 칸이다. 테이블의 1은 조각이 놓인 칸, 0은 빈 공간이다.
- 빈칸 덩어리와 조각은 1칸에서 6칸까지 연결된 형태로만 주어진다.
- 게임 보드에는 빈칸이 하나 이상, 테이블에는 조각이 하나 이상 있다.

입출력 예:

| game_board | table | result |
| --- | --- | --- |
| [[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]] | [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]] | 14 |
| [[0,0,0],[1,1,0],[1,1,1]] | [[1,1,1],[1,0,0],[0,0,0]] | 0 |

입출력 예 설명:

- 예 #1: 규칙에 맞게 최대한 채우면 14칸을 채울 수 있다.
- 예 #2: 블록의 회전은 가능하지만 뒤집을 수는 없어서 채울 수 있는 조각이 없다.

## 문제 분석 및 핵심 로직

이 문제는 "빈칸 덩어리(구멍)"와 "조각"을 각각 연결 요소로 보고, 모양이 같은 쌍을 찾는 문제이다. 핵심은 세 가지이다.

1. 게임 보드의 0인 칸들을 상하좌우 연결 기준으로 묶어 구멍 목록을 만든다. 테이블의 1인 칸들도 같은 방식으로 묶어 조각 목록을 만든다. 연결 요소 추출에는 BFS를 쓴다.
2. 모양을 비교할 때는 위치를 없앤다. 각 요소의 칸 좌표에서 가장 위·왼쪽 칸을 (0, 0)으로 옮겨 정규화하면, 보드 위 어디에 있든 같은 모양은 같은 좌표 집합이 된다.
3. 조각은 회전이 가능하므로, 한 조각마다 90도씩 네 번 회전한 정규화 모양을 모두 만들고 구멍 모양과 비교한다. 뒤집기는 금지이므로 좌우 반전 모양은 만들지 않는다. 칸 수가 다른 조각은 모양이 같을 수 없으므로 비교 전에 건너뛴다.

구멍마다 아직 쓰지 않은 조각 중 모양이 일치하는 것을 찾아 채우고, 채운 칸 수를 더한다. 구멍과 조각이 일대일로 대응하는 형태이므로, 탐욕적으로 순서대로 매칭해도 개수는 같다. 조각 하나가 들어갈 수 있는 구멍은 모양이 같은 구멍뿐이고, 모양이 같은 구멍끼리는 크기도 같아 어느 쪽에 넣든 채우는 칸 수가 동일하기 때문이다.

## 개념별 심층 설명

### 1. 왜 빈칸을 하나씩 보지 않고 덩어리로 묶는가

초심자 방식은 빈칸 하나하나에 조각을 대입해 보며 맞추는 것이다. 빈칸마다 조각을 회전시켜 가며 대입하면 경우의 수가 금방 커지고, 조각을 놓은 뒤 옆에 빈칸이 남지 않는다는 규칙까지 매번 검사해야 한다.

이 문제에서 빈칸은 상하좌우로 연결된 덩어리 단위로만 의미가 있다. 규칙상 조각을 놓은 뒤 인접한 칸에 빈칸이 남으면 안 되므로, 하나의 구멍은 정확히 같은 모양의 조각 하나로 통째로 채워야 한다. 구멍을 덩어리 단위로 묶으면 문제는 "모양이 같은 구멍과 조각을 짝짓는 일"로 단순해진다. 덩어리를 묶는 데는 BFS가 적당하다. 시작 칸에서 상하좌우로 같은 값인 칸을 계속 퍼뜨리면 하나의 덩어리가 완성되고, 방문 표시를 해 두면 같은 덩어리를 두 번 세지 않는다.

### 2. 정규화: 위치를 지워 모양만 남기는 이유

같은 L자 모양이라도 보드 왼쪽 위에 있느냐 오른쪽 아래에 있느냐에 따라 좌표는 완전히 다르다. 좌표 그대로 비교하면 같은 모양을 다르다고 판단한다.

정규화는 각 덩어리의 가장 위쪽 행과 가장 왼쪽 열을 0으로 옮기는 연산이다. 모든 칸에서 최소 행과 최소 열을 빼면, 덩어리는 원점 근처로 이동하고 위치 정보는 사라진다. 남은 것은 칸들의 상대적인 배치, 즉 모양뿐이다. 정규화된 모양은 집합으로 저장하는데, 집합은 순서가 없어 비교가 간단하고 중복된 칸이 있어도 자동으로 합쳐진다.

### 3. 회전은 네 번, 뒤집기는 하지 않는 이유

조각은 90도씩 회전시킬 수 있으므로 한 조각은 최대 네 가지 방향으로 놓일 수 있다. 90도 회전은 좌표 변환 `(r, c) -> (c, -r)`로 표현한다. 음수 좌표가 생기지만, 회전 후 다시 정규화하면 원점 근처로 돌아오므로 비교에 문제가 없다. 네 번 회전하면 원래 방향으로 돌아오므로 네 가지 모양이면 충분하다.

뒤집기는 규칙상 금지되어 있다. 좌우 반전은 `(r, c) -> (r, -c)` 같은 변환인데, 이것을 허용하면 뒤집어야만 맞는 조각까지 채울 수 있게 되어 예 #2 같은 경우에 답이 달라진다. 회전 모양만 만드는 것이 곧 규칙을 코드로 옮긴 것이다. 대칭인 모양은 네 번 회전해도 서로 겹치는 모양이 생기는데, 집합에 넣어 두면 중복이 자연스럽게 제거된다.

### 4. 칸 수로 먼저 거르는 이유

구멍과 조각의 칸 수가 다르면 모양이 같을 수 없다. 칸 수가 같은 경우에만 회전 모양을 비교하면, 모양 비교 횟수가 크게 줄어든다. 이 문제는 조각 크기가 최대 6칸으로 작지만, 보드가 50x50이라 구멍과 조각이 각각 수백 개까지 생길 수 있다. 칸 수 필터가 없으면 모든 구멍마다 모든 조각의 회전 모양을 비교해야 하므로, 이 한 줄의 거름이 전체 실행 시간을 좌우한다.

## 최종 솔루션 코드

### Python

```python
# 퍼즐 조각 채우기 (프로그래머스 84021)
# https://school.programmers.co.kr/learn/courses/30/lessons/84021
# 2026-11-12
from collections import deque


def solution(game_board, table):
    n = len(game_board)
    # 1. 게임 보드의 빈칸(0)들을 연결 요소(구멍)로 추출한다.
    holes = _extract(game_board, 0, n)
    # 2. 테이블의 조각(1)들을 연결 요소로 추출한다.
    pieces = _extract(table, 1, n)
    # 3. 각 구멍마다 회전시켜 모양이 일치하는 미사용 조각을 찾아 채운다.
    used = [False] * len(pieces)
    answer = 0
    for hole in holes:
        hole_shape = _normalize(hole)
        for i, piece in enumerate(pieces):
            if used[i] or len(piece) != len(hole):
                continue
            if hole_shape in _rotations(piece):
                used[i] = True
                answer += len(hole)
                break
    return answer


def _extract(board, target, n):
    visited = [[False] * n for _ in range(n)]
    components = []
    for r in range(n):
        for c in range(n):
            if board[r][c] != target or visited[r][c]:
                continue
            # BFS로 target 값이 상하좌우로 연결된 칸들을 한 요소로 모은다.
            comp = []
            q = deque([(r, c)])
            visited[r][c] = True
            while q:
                cr, cc = q.popleft()
                comp.append((cr, cc))
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < n and 0 <= nc < n \
                            and not visited[nr][nc] and board[nr][nc] == target:
                        visited[nr][nc] = True
                        q.append((nr, nc))
            components.append(comp)
    return components


def _normalize(cells):
    # 가장 위·왼쪽 칸을 (0, 0)으로 옮겨 위치와 무관한 모양만 남긴다.
    min_r = min(r for r, _ in cells)
    min_c = min(c for _, c in cells)
    return frozenset((r - min_r, c - min_c) for r, c in cells)


def _rotations(cells):
    # 뒤집기는 금지, 90도씩 네 번 회전한 정규화 모양을 모두 만든다.
    shapes = set()
    cur = list(cells)
    for _ in range(4):
        shapes.add(_normalize(cur))
        cur = [(c, -r) for r, c in cur]
    return shapes
```

### Java

```java
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
```

## 성능 측정

로컬 실측 (Python 3, Java JDK):

| 케이스 | Python | Java |
| --- | --- | --- |
| 입출력 예 #1 (6x6) | 0.100 ms/회 (1,000회 평균) | 0.123 ms/회 (1,000회 평균) |
| 50x50 현실적 보드 (1~6칸 조각 120개씩 배치) | 12.7 ms, 피크 메모리 43.0 KiB | — |
| 50x50 무작위 보드 (스트레스, 조각 크기 제한 없음) | 34.4 ms | 7.9 ms |

- 시간 복잡도: O(N² + H × P × K). N은 보드 한 변(최대 50), H는 구멍 수, P는 조각 수, K는 조각 크기(최대 6)이다. 추출은 보드 전체를 한 번씩 훑는 O(N²), 매칭은 칸 수가 같은 조각에 대해서만 최대 4회전 × K칸을 비교한다.
- 공간 복잡도: O(N²). 방문 표시 배열과 추출한 요소 목록이 보드 크기에 비례한다.

## 요약

- 빈칸과 조각을 BFS로 연결 요소 단위로 묶어, 문제를 모양 짝짓기로 바꾼다.
- 정규화로 위치를 지우고, 90도 회전 네 가지 모양만 비교해 뒤집기 금지 규칙을 지킨다.
- 칸 수가 다른 조각은 비교 전에 거른다.
- 막혔던 점: 없음. 처음부터 연결 요소 + 정규화 + 회전 비교로 설계했고, 예제 2개와 직접 만든 회전·불일치 케이스를 포함해 Python·Java 모두 통과했다.
- 핵심 포인트: 구멍은 통째로 채워야 한다는 규칙 덕분에, 빈칸 하나하나가 아니라 덩어리 모양 비교만으로 충분하다.

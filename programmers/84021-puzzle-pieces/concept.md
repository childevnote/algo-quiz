# 개념 정리: 연결 요소, 정규화, 회전

## 1. 연결 요소 (Connected Component)

격자에서 같은 값을 가진 칸들이 상하좌우로 이어진 덩어리를 연결 요소라고 한다. 대각선으로만 닿은 칸은 연결된 것으로 보지 않는다.

### BFS로 연결 요소 찾기

시작 칸을 큐에 넣고, 큐에서 칸을 꺼낼 때마다 상하좌우 이웃 중 아직 방문하지 않았고 같은 값을 가진 칸을 큐에 추가한다. 큐가 빌 때까지 반복하면 시작 칸과 연결된 모든 칸을 모을 수 있다. 방문 표시를 해 두면 이미 처리한 덩어리를 다시 세지 않는다.

```python
from collections import deque

def bfs(grid, sr, sc, visited):
    component = []
    q = deque([(sr, sc)])
    visited[sr][sc] = True
    while q:
        r, c = q.popleft()
        component.append((r, c))
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) \
                    and not visited[nr][nc] and grid[nr][nc] == grid[sr][sc]:
                visited[nr][nc] = True
                q.append((nr, nc))
    return component
```

전체 격자를 훑으며 방문하지 않은 칸마다 BFS를 시작하면 모든 연결 요소를 빠짐없이 얻을 수 있다. DFS(재귀)로도 같은 결과를 얻을 수 있지만, 덩어리가 커지면 재귀 깊이가 깊어져 스택 제한에 걸릴 수 있어 BFS가 안전하다.

## 2. 모양 정규화 (Normalization)

덩어리의 모양을 비교하려면 위치를 없애야 한다. 정규화는 덩어리의 가장 위쪽 행과 가장 왼쪽 열을 0으로 옮기는 연산이다. 모든 칸의 좌표에서 최소 행과 최소 열을 빼면, 덩어리는 원점 근처로 이동하고 남는 것은 칸들의 상대 배치, 즉 모양뿐이다.

```python
def normalize(cells):
    min_r = min(r for r, _ in cells)
    min_c = min(c for _, c in cells)
    return frozenset((r - min_r, c - min_c) for r, c in cells)
```

예를 들어 칸이 (2, 3), (2, 4), (3, 3)에 있는 덩어리는 정규화하면 (0, 0), (0, 1), (1, 0)이 된다. 보드 위 어디에 있든 같은 모양은 같은 집합이 되므로, 집합 동등성만으로 모양 비교가 끝난다.

## 3. 90도 회전과 뒤집기

### 90도 회전

격자 위의 점 (r, c)를 시계 방향으로 90도 회전하면 (c, -r)이 된다. 음수 좌표가 생길 수 있지만, 회전 후 정규화를 다시 하면 원점 근처로 돌아오므로 비교에 문제가 없다. 90도씩 네 번 회전하면 원래 방향으로 돌아오므로, 한 도형의 회전 모양은 최대 네 가지이다. 대칭인 도형은 네 번 회전해도 겹치는 모양이 생긴다.

```python
def rotations(cells):
    shapes = set()
    cur = list(cells)
    for _ in range(4):
        shapes.add(normalize(cur))
        cur = [(c, -r) for r, c in cur]
    return shapes
```

### 뒤집기 (반전)

뒤집기는 도형을 뒤집어 좌우 또는 상하를 바꾸는 변환이다. 예를 들어 좌우 반전은 (r, c)를 (r, -c)로 바꾼다. 회전만으로 만들 수 없는 모양이 뒤집기로는 만들어질 수 있다. 예를 들어 L자 도형을 뒤집으면 거울상 L자가 되는데, 이것은 회전으로는 얻을 수 없다. 회전과 뒤집기를 허용하는지를 구분하는 것은 모양 비교 문제에서 흔히 나오는 조건이므로, 문제의 규칙을 변환 목록에 정확히 반영해야 한다.

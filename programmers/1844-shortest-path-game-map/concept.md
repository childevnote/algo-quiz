# 개념 정리: 너비 우선 탐색(BFS)과 최단 거리

## 너비 우선 탐색(BFS)

BFS는 시작점에서 가까운 정점부터 순서대로 탐색하는 그래프 탐색 방법이다. 큐(선입선출)를 사용해 먼저 발견한 정점부터 처리하므로, 시작점으로부터의 거리가 가까운 정점이 항상 먼 정점보다 먼저 처리된다.

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```

- 큐에 들어간 순서가 곧 시작점으로부터의 거리 순이다.
- 간선의 가중치가 모두 같을 때, BFS로 처음 방문한 순간의 거리가 최단 거리다.
- 깊이 우선 탐색(DFS)은 한 갈래를 끝까지 파고들지만, BFS는 같은 깊이를 전부 처리한 뒤 다음 깊이로 넘어간다.

## 거리 배열로 방문 여부 겸하기

최단 거리를 구하는 BFS에서는 방문 여부를 별도로 두지 않고, 거리 배열 하나로 겸하는 방식이 자주 쓰인다.

```python
dist = [-1] * n          # -1: 미방문
dist[start] = 0          # 시작점 거리 0
queue = deque([start])
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if dist[neighbor] == -1:      # 아직 방문하지 않았으면
            dist[neighbor] = dist[node] + 1
            queue.append(neighbor)
```

- `-1`인 정점은 미방문, 그 외의 값은 이미 방문했고 그 값이 최단 거리다.
- 처음 방문할 때 기록되는 거리가 최단 거리인 이유는 BFS가 거리 순서대로 확장하기 때문이다.
- 답이 "이동 횟수"가 아니라 "지나간 정점 개수"라면 시작점 거리를 1로 두면 된다.

## 격자에서의 BFS

2차원 격자는 각 칸이 정점, 상하좌우 이동이 간선인 그래프다. 좌표 (x, y)의 이웃은 방향 배열로 열거한다.

```python
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 아래, 위, 오른쪽, 왼쪽

for dx, dy in directions:
    nx, ny = x + dx, y + dy
    if 0 <= nx < n and 0 <= ny < m:  # 격자 안쪽인지 확인
        # 벽 여부, 방문 여부를 추가로 검사
        pass
```

- 격자 밖으로 나가는 이동은 범위 검사로 막는다.
- 벽이 있는 칸은 이동 대상에서 제외한다.

## 도달 불가능 판정

BFS가 끝날 때까지 목표 정점에 도달하지 못하면, 시작점에서 목표 정점으로 가는 경로가 존재하지 않는다. 큐가 비었다는 것은 도달 가능한 정점을 모두 방문했다는 뜻이므로, 거리 배열의 목표 정점 값이 초기값 그대로 남아 있으면 도달 불가능으로 판정한다.

# 개념 정리 — 그래프 탐색(DFS/BFS)과 연결 요소

## 1. 그래프와 연결 요소

그래프는 정점(node)과 간선(edge)으로 이루어진 구조다. 무방향 그래프에서 두 정점이 간선을 따라 이동해 도달할 수 있으면 "연결되어 있다"고 한다. 직접 연결되지 않았어도 다른 정점을 거쳐 도달할 수 있으면 같은 연결 요소(connected component)에 속한다.

예를 들어 정점 A, B, C가 있고 간선이 A–B, B–C만 있어도 A와 C는 같은 연결 요소다. 간선이 하나도 없는 정점은 그 자체로 하나의 연결 요소다.

## 2. 깊이 우선 탐색(DFS)

DFS는 한 갈래를 끝까지 파고든 뒤 되돌아오는 탐색이다. 스택(재귀 호출 스택 또는 명시적 스택)을 이용해 구현한다.

일반적인 예시 — 스택 기반 DFS로 도달 가능한 정점 모두 방문:

```python
def dfs(start, graph):
    visited = set()
    stack = [start]
    visited.add(start)
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                stack.append(nxt)
    return visited
```

정점을 스택에 넣는 시점에 방문 처리하는 것이 중요하다. 꺼낼 때 방문 처리하면 같은 정점이 스택에 여러 번 들어가 중복 탐색이 생긴다.

## 3. 너비 우선 탐색(BFS)

BFS는 시작 정점에서 가까운 정점부터 순서대로 방문하는 탐색이다. 큐를 이용해 구현한다. 시작 정점으로부터의 최단 거리(간선 수 기준)를 구할 때 쓴다.

일반적인 예시 — 큐 기반 BFS:

```python
from collections import deque

def bfs(start, graph):
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for nxt in graph[node]:
            if nxt not in visited:
                visited.add(nxt)
                queue.append(nxt)
    return visited
```

DFS와 BFS는 "도달 가능한 정점을 빠짐없이 방문한다"는 점에서는 같다. 차이는 방문 순서뿐이다. 연결 요소의 개수만 셀 때는 어느 쪽을 써도 되고, 최단 거리가 필요할 때만 BFS를 써야 한다.

## 4. 인접 행렬 vs 인접 리스트

그래프를 표현하는 두 가지 대표적인 방식이다.

- **인접 행렬**: n × n 표로, `matrix[i][j] == 1`이면 i와 j가 연결되어 있다. 두 정점의 연결 여부를 O(1)에 확인할 수 있지만, 공간이 O(n²)이고 이웃을 찾으려면 행 하나를 전부 훑어야 한다.
- **인접 리스트**: 각 정점마다 연결된 이웃 목록을 저장한다. 공간이 간선 수에 비례하고 이웃만 골라 훑을 수 있어 간선이 희소한 그래프에 유리하다. 대신 두 정점의 연결 여부를 확인하려면 이웃 목록을 뒤져야 한다.

정점 수가 수백 이하이고 입력 자체가 행렬로 주어지면, 리스트로 변환하는 수고 없이 행렬을 그대로 쓰는 편이 낫다.

## 5. Union-Find(분리 집합) — 연결 요소를 세는 다른 방법

연결 요소의 개수는 DFS/BFS 없이 Union-Find로도 셀 수 있다. 각 정점을 처음에는 자기만의 집합으로 두고, 간선이 주어질 때마다 두 정점이 속한 집합을 합친다. 모든 간선을 처리한 뒤 서로 다른 집합의 개수가 곧 연결 요소의 개수다.

일반적인 예시:

```python
parent = list(range(n))

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra
```

Union-Find는 간선이 하나씩 추가되는 동적인 상황에서 강하다. 정적인 그래프의 연결 요소 개수만 구할 때는 DFS/BFS가 더 직관적이다.

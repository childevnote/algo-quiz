# 개념 정리: 순위 문제를 푸는 데 필요한 개념

## 1. 방향 그래프와 도달 가능성

방향 그래프는 정점(node)과 방향이 있는 간선(edge)으로 이루어진 구조다. 간선 u → v는 "u에서 v로 갈 수 있다"는 뜻이다. 도달 가능성(reachability)은 한 정점에서 간선을 따라 다른 정점에 도달할 수 있는지를 묻는 개념이다. 직접 간선이 없어도 중간 정점을 거쳐 갈 수 있으면 도달 가능하다고 본다.

일반적인 예시: 도시 A에서 도시 B로 가는 직행 열차가 없어도, A → C, C → B 열차가 있으면 A에서 B에 도달할 수 있다. 그래프에서는 이를 "A에서 B로 가는 경로가 존재한다"고 표현한다.

```python
# 인접 행렬로 방향 그래프 표현 (정점 0, 1, 2)
# graph[u][v] = True: u에서 v로 가는 간선이 있음
graph = [
    [False, True, False],   # 0 -> 1
    [False, False, True],   # 1 -> 2
    [False, False, False],
]
# 0에서 2로 가는 직접 간선은 없지만, 0 -> 1 -> 2 경로로 도달 가능하다
```

## 2. 전이적 폐쇄 (Transitive Closure)

전이적 폐쇄는 그래프에 "도달 가능한 모든 정점 쌍"을 간선으로 추가해 완성한 그래프다. 원래 간선이 없어도 경로가 존재하면 간선을 추가한다. 관계가 전이적일 때, 즉 "A와 B가 관계가 있고 B와 C가 관계가 있으면 A와 C도 관계가 있다"는 규칙이 성립할 때 의미가 있다.

일반적인 예시: "선배" 관계가 전이적이다. 철수가 영희의 선배이고 영희가 민수의 선배이면, 철수는 민수의 선배이기도 하다. 직접 선후배 기록만으로는 철수와 민수의 관계를 알 수 없지만, 전이적 폐쇄를 구하면 알 수 있다.

## 3. 플로이드-워셜 알고리즘 (Floyd-Warshall)

플로이드-워셜은 모든 정점 쌍 사이의 최단 경로(또는 도달 가능성)를 구하는 동적 프로그래밍 알고리즘이다. 중간 경유점 k를 하나씩 고정하고, i → k → j 경로가 존재하면 i → j를 연결(또는 거리를 갱신)한다.

동작 원리: k를 0부터 n-1까지 순서대로 늘려 간다. k 단계가 끝나면 "중간 정점을 k 이하의 정점으로만 사용하는 경로"가 모두 반영된다. k가 마지막 정점에 도달하면 모든 경로가 반영되어 폐쇄가 완성된다. 시간 복잡도는 O(n³), 공간 복잡도는 O(n²)이다.

```python
# 도달 가능성 버전의 플로이드-워셜
n = 3
reach = [[False] * n for _ in range(n)]
reach[0][1] = True
reach[1][2] = True

for k in range(n):
    for i in range(n):
        for j in range(n):
            if reach[i][k] and reach[k][j]:
                reach[i][j] = True
# 결과: reach[0][2] == True (0 -> 1 -> 2 경로)
```

이 알고리즘은 간선 가중치가 있는 경우 최단 거리를 구하는 데도 쓰인다. 그때는 도달 여부 대신 거리 값을 두고, `dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])` 점화식을 사용한다. 음수 사이클이 없는 그래프에서 동작한다.

## 4. BFS/DFS를 이용한 도달 가능성

전이적 폐쇄를 구하는 다른 방법은 각 정점에서 BFS(너비 우선 탐색)나 DFS(깊이 우선 탐색)를 돌려 도달 가능한 정점을 전부 찾는 것이다. 한 정점에서 시작해 간선을 따라 방문할 수 있는 모든 정점을 표시하면, 그 정점에서 도달 가능한 집합을 얻을 수 있다. 모든 정점에 대해 반복하면 전이적 폐쇄와 같은 정보를 얻는다.

시간 복잡도는 정점마다 BFS/DFS를 돌리므로 O(n × (n + m))이다. 여기서 m은 간선 수다. n이 작으면 플로이드-워셜과 큰 차이가 없고, 그래프가 희소하면 BFS/DFS 방식이 유리하다.

```python
from collections import deque

def reachable_from(start, graph):
    n = len(graph)
    visited = [False] * n
    queue = deque([start])
    visited[start] = True
    while queue:
        u = queue.popleft()
        for v in range(n):
            if graph[u][v] and not visited[v]:
                visited[v] = True
                queue.append(v)
    return visited
```

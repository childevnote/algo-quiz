# 프로그래머스 49189 가장 먼 노드
# https://school.programmers.co.kr/learn/courses/30/lessons/49189
# 2026-11-14

from collections import deque


def solution(n, edge):
    # 1. 인접 리스트 구성 (양방향 간선)
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)

    # 2. 1번 노드에서 BFS로 최단 거리 계산
    dist = [-1] * (n + 1)
    dist[1] = 0
    queue = deque([1])
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if dist[nxt] == -1:
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)

    # 3. 최대 거리와 같은 거리의 노드 개수 세기
    max_dist = max(dist[1:])
    return sum(1 for d in dist[1:] if d == max_dist)


if __name__ == "__main__":
    print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))  # 3

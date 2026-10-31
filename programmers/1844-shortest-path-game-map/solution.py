# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/1844
# 풀이 날짜: 2026-10-30 (18:00 자동 풀이)

from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    # 1. 방문 거리 배열: -1은 미방문, 시작 칸(0, 0)은 지나간 칸 1개로 초기화
    dist = [[-1] * m for _ in range(n)]
    dist[0][0] = 1
    # 2. BFS 큐: 시작 위치에서 출발
    queue = deque([(0, 0)])
    # 3. 네 방향 이동
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        x, y = queue.popleft()
        # 4. 목표 칸에 도달하면 그 즉시 거리가 최단 거리
        if x == n - 1 and y == m - 1:
            return dist[x][y]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 5. 맵 안쪽, 벽이 아니고, 아직 방문하지 않은 칸만 이동
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    # 6. 큐가 비도록 목표 칸에 도달하지 못하면 -1
    return -1

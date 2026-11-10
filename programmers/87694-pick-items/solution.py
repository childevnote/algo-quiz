# 아이템 줍기 (프로그래머스 87694)
# https://school.programmers.co.kr/learn/courses/30/lessons/87694
# 2026-11-10
from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102
    board = [[0] * SIZE for _ in range(SIZE)]

    # 1. 각 직사각형의 테두리를 보드에 표시한다 (좌표 2배 스케일).
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x in (x1, x2) or y in (y1, y2):
                    board[y][x] = 1

    # 2. 각 직사각형의 내부를 지운다. 겹친 직사각형의 내부에 들어간
    #    다른 직사각형의 테두리 조각도 함께 지워져 테두리만 남는다.
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * 2, y1 * 2, x2 * 2, y2 * 2
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[y][x] = 0

    # 3. BFS로 테두리를 따라 최단 경로를 탐색한다.
    sx, sy = characterX * 2, characterY * 2
    tx, ty = itemX * 2, itemY * 2
    dist = [[-1] * SIZE for _ in range(SIZE)]
    dist[sy][sx] = 0
    queue = deque([(sx, sy)])
    while queue:
        x, y = queue.popleft()
        # 4. 아이템에 도달하면 스케일된 거리를 2로 나눠 실제 거리를 반환한다.
        if (x, y) == (tx, ty):
            return dist[y][x] // 2
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE and board[ny][nx] == 1 and dist[ny][nx] == -1:
                dist[ny][nx] = dist[y][x] + 1
                queue.append((nx, ny))

    return -1

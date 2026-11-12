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

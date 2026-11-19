# https://school.programmers.co.kr/learn/courses/30/lessons/49190
# 2026-11-19

def solution(arrows):
    # 방향 0~7: 0=위, 1=오른쪽 위, 2=오른쪽, 3=오른쪽 아래,
    #          4=아래, 5=왼쪽 아래, 6=왼쪽, 7=왼쪽 위
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    # 정점과 간선을 기록한다. 대각선 이동이 간선 중간에서
    # 교차하는 경우를 잡기 위해 한 칸 이동을 절반씩 두 번 나눈다.
    visited_v = {(0, 0)}
    visited_e = set()
    x, y = 0, 0
    rooms = 0

    for a in arrows:
        for _ in range(2):  # 절반 이동 2회
            nx, ny = x + dx[a], y + dy[a]
            edge = ((x, y), (nx, ny)) if (x, y) < (nx, ny) else ((nx, ny), (x, y))
            if (nx, ny) in visited_v and edge not in visited_e:
                # 이미 들른 정점에 새 간선으로 도착하면 방 하나가 닫힌다
                rooms += 1
            visited_v.add((nx, ny))
            visited_e.add(edge)
            x, y = nx, ny

    return rooms

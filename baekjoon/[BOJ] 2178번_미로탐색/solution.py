from collections import deque
import sys

read = sys.stdin.readline

def bfs(maze, n, m):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] # 이동할 수 있는 네 방향 (하, 상, 우, 좌)
    queue = deque([(0, 0)]) # 시작 위치를 큐에 넣는다. (0,0)이 (1,1)에 해당
    maze[0][0] = 1 # 시작 위치를 방문 처리 (거리를 1로 설정)

    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1: # 도착 위치에 도달했으면
            return maze[x][y] # 현재 위치의 거리 값을 반환
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 미로 범위 안에 있고, 이동 가능한 칸이면
            if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
                queue.append((nx, ny)) # 큐에 추가
                maze[nx][ny] = maze[x][y] + 1 # 이동한 칸의 거리는 이전 칸의 거리 + 1

def sol():
    n, m = map(int, read().split())
    maze = [list(map(int, read().strip())) for _ in range(n)]

    print(bfs(maze, n, m))

sol()

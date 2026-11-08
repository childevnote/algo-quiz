# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 2026-11-05 (자동 풀이, 2026-11-08 커밋)

def solution(n, computers):
    # 1. 방문 여부를 기록할 배열
    visited = [False] * n
    # 2. 네트워크 개수
    count = 0

    # 3. 아직 방문하지 않은 컴퓨터가 있으면 새 네트워크 시작
    for start in range(n):
        if visited[start]:
            continue
        count += 1
        # 4. 스택 기반 DFS로 연결된 컴퓨터를 모두 방문
        stack = [start]
        visited[start] = True
        while stack:
            node = stack.pop()
            for nxt in range(n):
                if computers[node][nxt] == 1 and not visited[nxt]:
                    visited[nxt] = True
                    stack.append(nxt)
    return count

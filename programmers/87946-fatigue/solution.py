# 피로도
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/87946
# 풀이 날짜: 2026-10-23 (자동 풀이)

def solution(k, dungeons):
    answer = 0
    n = len(dungeons)
    visited = [False] * n

    def backtrack(fatigue, count):
        nonlocal answer
        # ① 현재까지 탐험한 던전 수로 정답 후보 갱신
        answer = max(answer, count)
        # ② 남은 던전 중 입장 조건(최소 필요 피로도)을 만족하는 것을
        #    전부 시도하고, 복귀 시 방문 상태를 되돌린다 (백트래킹)
        for i in range(n):
            req, cost = dungeons[i]
            if not visited[i] and fatigue >= req:
                visited[i] = True
                backtrack(fatigue - cost, count + 1)
                visited[i] = False

    backtrack(k, 0)
    return answer

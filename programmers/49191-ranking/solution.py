# 프로그래머스 49191 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/49191
# 풀이일: 2026-11-15

def solution(n, results):
    # 1. 승패 관계 행렬: win[i][j] = i번 선수가 j번 선수를 이김 (0-indexed)
    win = [[False] * n for _ in range(n)]
    for a, b in results:
        win[a - 1][b - 1] = True

    # 2. 플로이드-워셜로 승패 관계의 전이적 폐쇄 계산
    #    i가 k를 이기고 k가 j를 이기면 i는 j를 이긴다
    for k in range(n):
        for i in range(n):
            if win[i][k]:
                row_i = win[i]
                row_k = win[k]
                for j in range(n):
                    if row_k[j]:
                        row_i[j] = True

    # 3. 다른 모든 선수와 승패가 확정된 선수 카운트
    answer = 0
    for i in range(n):
        count = 0
        for j in range(n):
            if i == j:
                continue
            if win[i][j] or win[j][i]:
                count += 1
        if count == n - 1:
            answer += 1
    return answer

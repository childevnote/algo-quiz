# 프로그래머스 43105 정수 삼각형
# https://school.programmers.co.kr/learn/courses/30/lessons/43105
# 2026-11-06

def solution(triangle):
    # 1. 마지막 행을 누적 최대합 배열로 복사해 시작점으로 삼는다
    dp = triangle[-1][:]
    # 2. 아래 행부터 위로 올라가며 각 칸에 도달 가능한 최대합을 누적한다
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 3. 바로 아래 두 칸 중 더 큰 쪽과 현재 값을 더한다
            dp[j] = triangle[i][j] + max(dp[j], dp[j + 1])
    # 4. 꼭대기에 남은 값이 전체 경로의 최대합이다
    return dp[0]

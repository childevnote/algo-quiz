# https://school.programmers.co.kr/learn/courses/30/lessons/42898
# 등굣길 (Lv.3, DP) — 2026-11-07

MOD = 1_000_000_007


def solution(m, n, puddles):
    # puddles 좌표는 [x, y] (x: 열 1..m, y: 행 1..n)
    puddle = set(map(tuple, puddles))
    # dp[y][x]: (1, 1)에서 (x, y)까지 도달하는 최단 경로 수
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if (x, y) in puddle:
                dp[y][x] = 0
                continue
            if x == 1 and y == 1:
                continue
            # 오른쪽·아래쪽 이동만 가능하므로, 위쪽과 왼쪽에서 오는 경우의 합
            dp[y][x] = (dp[y - 1][x] + dp[y][x - 1]) % MOD
    return dp[n][m]

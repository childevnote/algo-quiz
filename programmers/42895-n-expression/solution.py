# 프로그래머스 42895 N으로 표현
# https://school.programmers.co.kr/learn/courses/30/lessons/42895
# 풀이 날짜: 2026-11-05 (18:00 자동 풀이)

def solution(N, number):
    # 1. dp[i]: N을 i번 사용해서 만들 수 있는 수들의 집합
    dp = [set() for _ in range(9)]
    for i in range(1, 9):
        # 2. N을 i번 이어붙인 수 (예: N=5, i=3 -> 555)
        dp[i].add(int(str(N) * i))
        # 3. i번을 j번과 i-j번으로 나눠 사칙연산으로 조합
        for j in range(1, i):
            for a in dp[j]:
                for b in dp[i - j]:
                    dp[i].add(a + b)
                    dp[i].add(a - b)
                    dp[i].add(a * b)
                    if b != 0:
                        dp[i].add(a // b)
        # 4. number를 처음 만든 횟수가 최솟값
        if number in dp[i]:
            return i
    return -1

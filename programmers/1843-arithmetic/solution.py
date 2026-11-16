# 프로그래머스 1843 - 사칙연산
# https://school.programmers.co.kr/learn/courses/30/lessons/1843
# 풀이일: 2026-11-16

def solution(arr):
    # 1. 숫자와 연산자를 분리한다 (arr는 숫자, 연산자, 숫자, ... 형태)
    nums = [int(arr[i]) for i in range(0, len(arr), 2)]
    ops = [arr[i] for i in range(1, len(arr), 2)]
    n = len(nums)

    # 2. 구간 [i, j]의 최댓값/최솟값을 저장하는 DP 테이블
    NEG = float('-inf')
    POS = float('inf')
    mx = [[NEG] * n for _ in range(n)]
    mn = [[POS] * n for _ in range(n)]
    for i in range(n):
        mx[i][i] = mn[i][i] = nums[i]

    # 3. 길이가 짧은 구간부터 채운다
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            # 4. 마지막 연산 위치 k로 구간을 둘로 나눈다
            for k in range(i, j):
                if ops[k] == '+':
                    # 5a. 덧셈: 최대+최대, 최소+최소
                    mx[i][j] = max(mx[i][j], mx[i][k] + mx[k + 1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] + mn[k + 1][j])
                else:
                    # 5b. 뺄셈: 최대-최소, 최소-최대 (뺄셈은 뒤쪽이 작을수록 커진다)
                    mx[i][j] = max(mx[i][j], mx[i][k] - mn[k + 1][j])
                    mn[i][j] = min(mn[i][j], mn[i][k] - mx[k + 1][j])

    return mx[0][n - 1]

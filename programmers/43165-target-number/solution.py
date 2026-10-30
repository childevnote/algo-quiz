# 프로그래머스 43165 타겟 넘버
# https://school.programmers.co.kr/learn/courses/30/lessons/43165
# 풀이 날짜: 2026-10-29 (18:00 자동 풀이)

def solution(numbers, target):
    # 1. 재귀 DFS: 각 숫자를 더하거나 빼는 두 갈래로 탐색
    def dfs(idx, total):
        # 2. 모든 숫자를 사용했으면 합이 target인지 확인
        if idx == len(numbers):
            return 1 if total == target else 0
        # 3. 현재 숫자를 더하는 경우와 빼는 경우를 합산
        return dfs(idx + 1, total + numbers[idx]) + dfs(idx + 1, total - numbers[idx])

    return dfs(0, 0)

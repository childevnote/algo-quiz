# 프로그래머스 42897 도둑질
# https://school.programmers.co.kr/learn/courses/30/lessons/42897
# 풀이일: 2026-11-17


def solution(money):
    def rob(start, end):
        # money[start..end] 구간(직선 배치)에서 털 수 있는 최대 금액
        prev2 = 0  # 두 집 전까지 턴 최대 금액
        prev1 = 0  # 바로 전 집까지 턴 최대 금액
        for i in range(start, end + 1):
            prev2, prev1 = prev1, max(prev1, prev2 + money[i])
        return prev1

    # 첫 집을 털면 마지막 집을 털 수 없고, 마지막 집을 털면 첫 집을 털 수 없다.
    # 원형을 두 개의 직선 구간으로 나눠 각각의 최댓값 중 큰 쪽을 택한다.
    return max(rob(0, len(money) - 2), rob(1, len(money) - 1))

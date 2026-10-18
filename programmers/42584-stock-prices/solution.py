# https://school.programmers.co.kr/learn/courses/30/lessons/42584
# 주식가격 (스택/큐, Lv.2)
# 2026-10-17


def solution(prices):
    n = len(prices)
    ans = [0] * n
    stack = []  # ① 가격이 아직 떨어지지 않은 인덱스들을 보관 (비내림차순 스택)

    for i, price in enumerate(prices):
        # ② 스택 꼭대기의 가격보다 현재 가격이 낮으면 → 그 가격의 유지 기간 확정
        while stack and prices[stack[-1]] > price:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)  # ③ 현재 인덱스를 스택에 남겨 둠

    # ④ 스택에 남은 인덱스는 끝까지 가격이 떨어지지 않았으므로 남은 길이로 채움
    while stack:
        j = stack.pop()
        ans[j] = n - 1 - j

    return ans

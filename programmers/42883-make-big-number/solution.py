# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42883
# 날짜: 2026-10-24 (출제일) / 풀이·커밋: 2026-10-27 (18:00 자동 풀이)


def solution(number, k):
    # 1. 단조 감소 스택: 앞자리부터 쌓으면서, 현재 숫자보다 작은 스택 상단은
    #    제거 기회(k)가 남아 있는 한 제거한다. 앞자리가 클수록 전체 수가 커지기 때문이다.
    stack = []
    for digit in number:
        while k > 0 and stack and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    # 2. 제거 기회가 남았으면(전체가 내림차순인 경우) 뒤에서 자른다.
    #    뒤를 자르는 것이 가장 작은 손해이기 때문이다.
    if k > 0:
        stack = stack[:-k]
    # 3. 남은 스택을 그대로 이어붙인다. 순서가 곧 원래 상대 순서이다.
    return "".join(stack)

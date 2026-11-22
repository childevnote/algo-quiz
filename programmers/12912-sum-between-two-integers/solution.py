# https://school.programmers.co.kr/learn/courses/30/lessons/12912
# 2026-11-21

def solution(a, b):
    # 1. a와 b의 대소관계가 정해져 있지 않으므로 작은 쪽을 lo, 큰 쪽을 hi로 둔다.
    # 2. lo부터 hi까지의 합은 등차수열의 합: 항의 개수 n = hi - lo + 1,
    #    합 = n * (lo + hi) / 2. n * (lo + hi)는 항상 짝수이므로 정수 나눗셈이 안전하다.
    lo, hi = (a, b) if a <= b else (b, a)
    n = hi - lo + 1
    return n * (lo + hi) // 2

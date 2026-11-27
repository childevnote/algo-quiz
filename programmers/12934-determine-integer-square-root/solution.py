# 프로그래머스 12934 - 정수 제곱근 판별
# https://school.programmers.co.kr/learn/courses/30/lessons/12934
# 풀이 날짜: 2026-11-27

import math

def solution(n):
    # 1. n의 정수 제곱근 x를 구한다. (isqrt는 부동소수점 오차 없이 정확한 정수 제곱근을 반환한다)
    # 2. x의 제곱이 n과 같으면 완전제곱수이므로 (x+1)의 제곱을 반환한다.
    # 3. 다르면 -1을 반환한다.
    x = math.isqrt(n)
    return (x + 1) ** 2 if x * x == n else -1

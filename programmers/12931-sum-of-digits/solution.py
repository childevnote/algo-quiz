# 프로그래머스 12931 자릿수 더하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12931
# 2026-11-24

def solution(n):
    # 1. 10으로 나눈 나머지가 일의 자리 숫자이다.
    # 2. 10으로 나눈 몫으로 자리수를 한 칸씩 줄여 나간다.
    # 3. n이 0이 되면 모든 자릿수를 더한 것이다.
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

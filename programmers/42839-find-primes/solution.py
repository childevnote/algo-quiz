# https://school.programmers.co.kr/learn/courses/30/lessons/42839
# 2026-10-21

from itertools import permutations


def solution(numbers):
    # [1] 모든 길이의 순열을 만들어 후보 숫자를 만든다
    candidates = set()
    for length in range(1, len(numbers) + 1):
        for p in permutations(numbers, length):
            candidates.add(int("".join(p)))  # "011" -> 11 처럼 앞 0은 자동 소거

    # [2] 소수만 셈한다
    return sum(1 for n in candidates if is_prime(n))


def is_prime(n):
    # [3] 에라토스테네스식 약수 판정: sqrt(n)까지만 나눈다
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


if __name__ == "__main__":
    assert solution("17") == 3
    assert solution("011") == 2
    assert solution("2") == 1
    assert solution("0") == 0
    assert solution("1111111") == 1
    print("all ok")

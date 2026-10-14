# https://school.programmers.co.kr/learn/courses/30/lessons/42578
# 2026-10-14
from collections import Counter


def solution(clothes):
    # 1. 종류별 의상 개수를 센다
    counts = Counter(kind for _, kind in clothes)
    # 2. 종류마다 (개수 + 1)가지 선택지(해당 종류를 안 입는 경우 포함)를 곱하고,
    #    모든 종류를 안 입는 1가지 경우를 뺀다
    answer = 1
    for c in counts.values():
        answer *= (c + 1)
    return answer - 1

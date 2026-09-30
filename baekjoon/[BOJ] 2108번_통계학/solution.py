# 14:26 -
import sys
from collections import Counter

read = sys.stdin.readline


def Mean(num):  # 산술 평균
    return int(round(sum(num) / len(num), 0))


def Median(num):  # 중앙값
    sorted_num = sorted(num)
    return sorted_num[int(len(num) / 2)]


def Mode(num):  # 최빈값
    counts = Counter(num)
    max_count = max(counts.values())
    mode_values = sorted([value for value, count in counts.items() if count == max_count])
    return mode_values[1] if len(mode_values) > 1 else mode_values[0]


def Scope(num):  # 범위
    return max(num) - min(num)


def solution():
    n = int(read())
    num = [int(read()) for _ in range(n)]
    print(f"{Mean(num)}\n{Median(num)}\n{Mode(num)}\n{Scope(num)}")


solution()

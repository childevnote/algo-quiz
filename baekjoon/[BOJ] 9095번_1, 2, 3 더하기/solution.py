# 14:30
import sys

read = sys.stdin.readline


def initialization():
    d = [0] * 11
    d[0] = 1
    for i in range(1, 11):
        if i - 1 >= 0:
            d[i] += d[i - 1]
        if i - 2 >= 0:
            d[i] += d[i - 2]
        if i - 3 >= 0:
            d[i] += d[i - 3]
    return d


def solution():
    d = initialization()
    n = int(read())
    num = [list(map(int, read().split())) for _ in range(n)]
    for i in num:
        for j in i:
            print(d[j])


solution()

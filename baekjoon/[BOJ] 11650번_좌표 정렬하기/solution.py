import sys

read = sys.stdin.readline


def solution():
    n = int(read())
    points = [tuple(map(int, read().split())) for _ in range(n)]
    points.sort()
    for a, b in points:
        print(a, b)


solution()

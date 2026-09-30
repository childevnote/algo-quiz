import sys

read = sys.stdin.readline


def solution():
    n = int(read())
    points = [tuple(map(int, read().split())) for _ in range(n)]
    points.sort(key=lambda x: (x[1], x[0]))
    for a, b in points:
        print(a, b)


solution()

# 11:00 ~ 12:30
import sys

read = sys.stdin.readline


def findLessOil(index, oil):
    for o in range(index + 1, len(oil)):
        if oil[o] < oil[index]:
            return o
    return 0


def partCost(now, then, dist, oil):
    return sum(dist[now:then]) * oil[now]


def solution():
    n = int(read())
    dist = list(map(int, read().split()))
    oil = list(map(int, read().split()))
    cost = 0
    start = 0

    while start <= len(oil) - 1:
        j = findLessOil(start, oil)
        if j != 0:
            cost += partCost(start, j, dist, oil)
            start += j - start
        else:
            cost += partCost(start, len(oil), dist, oil)
            break
    print(cost)


solution()

import sys

read = sys.stdin.readline


def multiple(a, b, arr):
    mul = 1
    for i in range(a, b):
        mul *= arr[i]
    return mul


def sumMultiple(i, j, k, l, arr):
    return multiple(i, j, arr) + multiple(j, k, arr) + multiple(k, l, arr) + multiple(l, len(arr), arr)


def solution():
    n = int(read())
    arr = tuple(map(int, read().split()))
    max_value = 0
    for i in range(0, 1):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if sumMultiple(i, j, k, l, arr) > max_value:
                        max_value = sumMultiple(i, j, k, l, arr)
    print(max_value)


solution()

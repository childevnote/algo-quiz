import sys

read = sys.stdin.readline


def solution():
    n = int(read())
    num_n = set(map(int, read().split()))
    m = int(read())
    num_m = list(map(int, read().split()))

    for i in num_m:
        if i in num_n:
            print(1)
        else:
            print(0)


solution()

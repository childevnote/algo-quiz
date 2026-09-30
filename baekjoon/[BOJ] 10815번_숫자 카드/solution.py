import sys

read = sys.stdin.readline


def solution():
    n = int(read())
    num_n = set(map(int, read().split()))
    m = int(read())
    num_m = list(map(int, read().split()))
    answer = []
    for i in range(m):
        if num_m[i] in num_n:
            answer.append(1)
        else:
            answer.append(0)
    print(*answer)


solution()

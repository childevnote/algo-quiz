import sys

read = sys.stdin.readline


def solution():
    n = int(read())
    count = 0
    while n > 0:
        if n % 5 == 0:
            return n // 5 + count
        n -= 2
        count += 1
    if n == 0:
        return count
    else:
        return -1


print(solution())

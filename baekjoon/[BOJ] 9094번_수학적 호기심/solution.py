# 10:00 - 10:06
import sys

read = sys.stdin.readline


def solution():
    t = int(read())
    nm = [list(map(int, read().split())) for _ in range(t)]

    for num in nm:
        count = 0
        for a in range(1, num[0] - 1):
            for b in range(a + 1, num[0]):
                if (a * a + b * b + num[1]) % (a * b) == 0:
                    count += 1
        print(count)


solution()

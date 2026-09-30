# 22:04 ~ 22:24
import sys

read = sys.stdin.readline
write = sys.stdout.writelines


def solution():
    n, m = map(int, read().split())
    listen = set(read() for _ in range(n))
    answer = []
    count = 0
    for i in range(m):
        look = read()
        if look in listen:
            count += 1
            answer.append(look)
    print(count)
    write(sorted(answer))


solution()

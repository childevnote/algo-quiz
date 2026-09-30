import sys
from collections import deque

read = sys.stdin.readline


def solution():
    n = int(read())
    que = deque([])
    for i in range(n):
        que.append(i + 1)
    t = 1

    for i in range(n-1):
        num = (t**3)%len(que)
        if num == 1:
            que.popleft()
        else:
            que.rotate(-(num-1))
            que.popleft()
        t+=1
    print(*que)
solution()

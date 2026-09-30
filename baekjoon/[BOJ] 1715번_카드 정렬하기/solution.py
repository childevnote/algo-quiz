# 10:52 - 12:00, 14:20 -

import sys
import heapq

read = sys.stdin.readline


def solution():
    n = int(read())
    card = []
    for i in range(n):
        heapq.heappush(card, int(read()))
    count = 0
    while len(card) > 1:
        a = heapq.heappop(card)
        b = heapq.heappop(card)
        print(a, b)
        bundle = a + b
        count += bundle
        heapq.heappush(card, bundle)

    print(count)


solution()

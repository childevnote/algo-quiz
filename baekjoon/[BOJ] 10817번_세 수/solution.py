import sys

read = sys.stdin.readline()


def solution():
    abc = list(map(int, read.split()))
    abc = sorted(abc)
    print(abc[1])


solution()

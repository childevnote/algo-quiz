import sys

read = sys.stdin.readline


def sol():
    n, k = list(map(int, read().split()))
    googoodan = []
    for i in range(k):
        googoodan.append(int(str(n * (i + 1))[::-1]))

    print(max(googoodan))


sol()

import sys

read = sys.stdin.readline

def sol():
    n = list(read().strip())
    n.sort(reverse=True)

    if sum(map(int, n)) % 3 != 0:
        print(-1)
        return

    if n[-1] != '0':
        print(-1)
        return

    print(''.join(n))
    return

sol()
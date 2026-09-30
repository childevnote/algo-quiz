import sys

read = sys.stdin.readline

def sol():
    n = int(read())
    arr = [list(map(str,read().split())) for _ in range(n)]
    arr = sorted(arr,key=lambda x:(int(x[3]), int(x[2]), int(x[1])))
    print(arr[-1][0])
    print(arr[0][0])

sol()

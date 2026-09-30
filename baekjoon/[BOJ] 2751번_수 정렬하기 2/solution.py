import sys
read = sys.stdin.readline

def solution():
    n = int(read())
    num = [int(read()) for _ in range(n)]
    num = sorted(num)
    [print(i) for i in num]

solution()

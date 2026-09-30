# 11:18 ~ 11:35
def solution():
    t = int(input())
    for i in range(t):
        tc = int(input())
        q = tc//25
        d = (tc % 25)//10
        n = ((tc % 25) % 10)//5
        p = tc % 5
        print(f"{q} {d} {n} {p}")


solution()
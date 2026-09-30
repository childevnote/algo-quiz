def sol():
    T = int(input())
    for _ in range(T):
        X, Y = map(int, input().split())
        a = list(map(int, input().split()))

        found = False
        for mask in range(1 << 5):
            total = 0
            for i in range(5):
                if mask & (1 << i):
                    total += a[i]
            if X <= total <= Y:
                found = True
                break
        print("YES" if found else "NO")
sol()

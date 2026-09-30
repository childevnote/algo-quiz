# 11:10 ~ 13:30
def solution():
    n = int(input())
    tc = [int(input()) for _ in range(n)]
    triangular = [int(i * (i + 1) / 2) for i in range(1, 40)]

    for i in range(len(tc)):
        eureka = 0
        for j in range(len(triangular)):
            for k in range(j, len(triangular)):
                for l in range(k, len(triangular)):
                    if triangular[j]+triangular[k]+triangular[l] == tc[i]:
                        eureka = 1
        print(eureka)


solution()
# 12:30 ~ 12:37
def solution():
    t = int(input())
    btn = [300, 60, 10]
    min_btn = []
    for i in range(3):
        if t >= btn[i]:
            min_btn.append(t // btn[i])
            t = t % btn[i]
        else:
            min_btn.append(0)
    if t==0:
        for j in min_btn:
            print(j)
    else:
        print(-1)
solution()

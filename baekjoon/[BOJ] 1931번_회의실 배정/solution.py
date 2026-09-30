import sys
read = sys.stdin.readline
def solution():
    answer = 0
    n = int(read())
    schedule = [list(map(int, read().split())) for _ in range(n)]
    schedule = sorted(schedule, key=lambda s: (s[1], s[0]))
    end_time = 0

    for i in schedule:
        if i[0] >= end_time:
            answer += 1
            end_time = i[1]
    print(answer)

solution()

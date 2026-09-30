import sys

read = sys.stdin.readline


def solution():
    t = int(read())
    answer = []
    for _ in range(t):
        n = int(read())
        ranking = [tuple(map(int, read().split())) for _ in range(n)]
        ranking.sort()
        count = 1
        min_interview_rank = ranking[0][1]

        for i in range(1, n):
            if ranking[i][1] < min_interview_rank:
                count += 1
                min_interview_rank = ranking[i][1]
        answer.append(count)
    [print(i) for i in answer]


solution()

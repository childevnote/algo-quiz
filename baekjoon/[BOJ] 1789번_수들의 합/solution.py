def solution():
    n = int(input())
    answer = 0
    temp = 0
    for i in range(1, n+1):
        temp += i
        answer += 1
        if temp > n:
            return answer-1
        elif temp == n:
            return answer


print(solution())

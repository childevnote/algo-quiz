def solution():
    s = input()
    answer = []
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            answer.append(s[i-1])

    if answer and s[-1] != answer[-1]:
        answer.append(s[-1])

    print(min(answer.count('0'), answer.count('1')))

solution()
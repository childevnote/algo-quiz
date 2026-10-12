# https://school.programmers.co.kr/learn/courses/30/lessons/12909
# 2026-10-11

def solution(s):
    balance = 0
    for c in s:
        if c == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

# 11:10 ~ 11:55
import sys
read = sys.stdin.readline

def sum_calculator(s):
    total = 0
    for i in s.split('+'):
        total += int(i)
    return total

def solution():
    formula = read()
    formula = formula.split('-')
    answer = sum_calculator(formula[0])

    for i in range(1, len(formula)):
        answer -= sum_calculator(formula[i])

    print(answer)

solution()
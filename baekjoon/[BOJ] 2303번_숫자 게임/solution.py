# 16:05 ~ 16:44
import sys
read = sys.stdin.readline
def solution():
    # 입력 받기
    n = int(read())
    arr = [list(map(int, read().split())) for _ in range(n)]
    who = []  # 누가 이겼는지 값과 인덱스를 관리하기 위한 배열
    for i in range(n):
        digits = 0  # 각 사람의 3장의 카드의 숫자의 합의 일의 자리 수의 최댓값
        for j in range(len(arr[i])):
            for k in range(j + 1, len(arr[i])):
                for l in range(k + 1, len(arr[i])):
                    this_digit = (arr[i][j] + arr[i][k] + arr[i][l]) % 10
                    if this_digit > digits:
                        digits = this_digit
        who.append(digits)
    # who의 인덱스와 값을 확인하여 최댓값을 가진 인덱스들 중 가장 큰 인덱스 출력
    print(max([i for i, v in enumerate(who) if v == max(who)]) + 1)

solution()

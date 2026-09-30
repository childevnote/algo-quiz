import sys

read = sys.stdin.readline


def solution():
    index = 1
    answer = []
    while True:
        num = list(map(int, read().split()))
        if num[0] != 0:
            answer.append((index, num))

        else:
            break
        index += 1

    for index, num in answer:
        if num[2] % num[1] < num[0]:
            print(f"Case {index}: {(num[2] // num[1]) * num[0] + num[2] % num[1]}")
        else:
            print(f"Case {index}: {((num[2] // num[1]) + num[0]) * num[0]}")


solution()

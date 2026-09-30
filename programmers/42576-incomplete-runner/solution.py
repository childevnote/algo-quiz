# 프로그래머스 42576 완주하지 못한 선수
# https://school.programmers.co.kr/learn/courses/30/lessons/42576
# 2026-09-30

from collections import Counter

def solution(participant, completion):
    count = Counter(participant)
    count.subtract(completion)
    for name, c in count.items():
        if c > 0:
            return name

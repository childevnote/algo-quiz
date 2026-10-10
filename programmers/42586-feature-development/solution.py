# 프로그래머스 42586 기능개발
# https://school.programmers.co.kr/learn/courses/30/lessons/42586
# 2026-10-10

import math

def solution(progresses, speeds):
    # 1. 각 작업이 완성되기까지 남은 일수 계산 (올림)
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    # 2. 앞 작업의 배포일을 넘지 못하면 함께 배포, 넘으면 새 배포
    answer = []
    cur_day, count = days[0], 1
    for d in days[1:]:
        if d <= cur_day:
            count += 1
        else:
            answer.append(count)
            cur_day, count = d, 1
    answer.append(count)
    return answer

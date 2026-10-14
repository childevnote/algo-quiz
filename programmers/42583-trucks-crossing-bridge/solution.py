# https://school.programmers.co.kr/learn/courses/30/lessons/42583
# 2026-10-14
from collections import deque


def solution(bridge_length, weight, truck_weights):
    bridge = deque()  # (트럭 무게, 다리를 완전히 나가는 시각)
    total = 0         # 다리 위 트럭들의 무게 합
    time = 0
    waiting = deque(truck_weights)

    while waiting or bridge:
        time += 1
        # 1. 나가는 시각이 된 트럭을 다리에서 내린다
        if bridge and bridge[0][1] == time:
            total -= bridge.popleft()[0]
        # 2. 대기 중인 첫 트럭이 진입 조건(빈자리, 무게 여유)을 만족하면 올린다
        if waiting and len(bridge) < bridge_length and total + waiting[0] <= weight:
            w = waiting.popleft()
            bridge.append((w, time + bridge_length))
            total += w
    return time

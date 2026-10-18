# 더 맵게 — https://school.programmers.co.kr/learn/courses/30/lessons/42626
# 2026-10-18 (18:00 자동 풀이)
import heapq


def solution(scoville, K):
    heapq.heapify(scoville)  # 1. 전체를 최소 힙으로
    answer = 0
    while scoville[0] < K:  # 2. 가장 안 매운 게 K 미만이면 계속 섞음
        if len(scoville) < 2:  # 3. 섞을 수 없으면 -1
            return -1
        first = heapq.heappop(scoville)  # 4. 가장 안 매운 두 개
        second = heapq.heappop(scoville)
        heapq.heappush(scoville, first + 2 * second)  # 5. 섞은 음식 투입
        answer += 1
    return answer

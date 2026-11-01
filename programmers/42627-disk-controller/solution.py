# 프로그래머스 42627 디스크 컨트롤러
# https://school.programmers.co.kr/learn/courses/30/lessons/42627
# 풀이 날짜: 2026-11-01

import heapq


def solution(jobs):
    # 1. 요청 시각 순으로 정렬 (작업 번호는 원래 인덱스)
    indexed = [(s, l, i) for i, (s, l) in enumerate(jobs)]
    indexed.sort()
    n = len(jobs)

    heap = []  # 2. 대기 큐: (소요시간, 요청시각, 작업번호) 순 최소 힙
    idx = 0
    time = 0
    total = 0

    # 3. 모든 작업이 끝날 때까지 시뮬레이션
    while idx < n or heap:
        # 대기 큐가 비어 있으면 다음 작업 요청 시각으로 점프
        if not heap:
            time = max(time, indexed[idx][0])
        # 현재 시각까지 요청된 작업을 모두 대기 큐에 삽입
        while idx < n and indexed[idx][0] <= time:
            s, l, i = indexed[idx]
            heapq.heappush(heap, (l, s, i))
            idx += 1
        # 우선순위 가장 높은 작업(소요시간 최단) 실행
        l, s, i = heapq.heappop(heap)
        time += l
        total += time - s  # 반환 시간 = 종료 시각 - 요청 시각

    return total // n

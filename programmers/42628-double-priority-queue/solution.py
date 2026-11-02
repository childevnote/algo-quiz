# 프로그래머스 42628 이중우선순위큐
# https://school.programmers.co.kr/learn/courses/30/lessons/42628
# 풀이 날짜: 2026-11-02

import heapq


def solution(operations):
    min_heap = []  # 1. 최솟값 꺼내기용 최소 힙
    max_heap = []  # 2. 최댓값 꺼내기용 최대 힙 (음수 저장)
    count = {}     # 3. 값이 실제로 큐에 몇 개 남아 있는지 세는 딕셔너리

    for op in operations:
        cmd, num_str = op.split()
        num = int(num_str)

        if cmd == "I":
            # 삽입: 두 힙 모두에 넣고 개수 기록
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count[num] = count.get(num, 0) + 1
        elif num == 1:
            # 4. 최댓값 삭제: 이미 삭제된 stale 원소를 건너뛰고 pop
            while max_heap and count.get(-max_heap[0], 0) == 0:
                heapq.heappop(max_heap)
            if max_heap:
                count[-heapq.heappop(max_heap)] -= 1
        else:  # num == -1
            # 5. 최솟값 삭제: 같은 방식으로 최소 힙에서 pop
            while min_heap and count.get(min_heap[0], 0) == 0:
                heapq.heappop(min_heap)
            if min_heap:
                count[heapq.heappop(min_heap)] -= 1

    # 6. 양쪽 힙의 top을 stale 원소 없이 정리
    while max_heap and count.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and count.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    if not max_heap:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]

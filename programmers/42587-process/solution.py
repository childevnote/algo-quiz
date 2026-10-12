# 프로그래머스 42587 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 2026-10-12

from collections import deque


def solution(priorities, location):
    # (원래 위치, 우선순위) 쌍을 담는 실행 대기 큐
    queue = deque(enumerate(priorities))
    # 1. 우선순위별 남은 개수 (우선순위는 1~9로 고정)
    freq = [0] * 10
    for p in priorities:
        freq[p] += 1
    # 2. 현재 큐에 남아 있는 최대 우선순위
    highest = 9
    while freq[highest] == 0:
        highest -= 1
    order = 0
    while queue:
        idx, p = queue.popleft()
        if p < highest:
            # 3. 더 높은 우선순위가 남아 있으면 맨 뒤로 보냄
            queue.append((idx, p))
        else:
            # 4. 실행 확정 (다시 큐에 넣지 않음)
            order += 1
            freq[p] -= 1
            if idx == location:
                return order
            # 5. 실행된 우선순위가 소진되면 최대값 갱신
            while highest > 0 and freq[highest] == 0:
                highest -= 1


if __name__ == "__main__":
    assert solution([2, 1, 3, 2], 2) == 1
    assert solution([1, 1, 9, 1, 1, 1], 0) == 5
    assert solution([1], 0) == 1
    assert solution([3, 2, 1], 2) == 3
    assert solution([9, 1, 1, 1], 3) == 4
    print("all tests passed")

# 프로그래머스 43236 징검다리
# https://school.programmers.co.kr/learn/courses/30/lessons/43236
# 풀이일: 2026-11-18

def solution(distance, rocks, n):
    # 1. 바위를 위치 순으로 정렬하고 도착지점을 마지막 지점으로 추가
    rocks = sorted(rocks)
    rocks.append(distance)

    # 2. 정답(제거 후 최소 거리)에 대한 이분탐색
    lo, hi = 1, distance
    answer = 0
    while lo <= hi:
        mid = (lo + hi) // 2
        # 3. 최소 거리를 mid로 유지하려면 몇 개의 바위를 제거해야 하는지 셈
        removed = 0
        prev = 0  # 마지막으로 남긴 지점 (출발지점 0부터)
        for rock in rocks:
            if rock - prev < mid:
                removed += 1  # 간격이 부족하면 이 바위를 제거
            else:
                prev = rock  # 간격이 충분하면 이 바위를 남김
        # 4. 제거 개수가 n 이하이면 mid는 달성 가능 -> 더 큰 값 시도
        if removed <= n:
            answer = mid
            lo = mid + 1
        else:
            hi = mid - 1
    return answer

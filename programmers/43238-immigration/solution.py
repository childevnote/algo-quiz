# 프로그래머스 43238 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# 날짜: 2026-11-13


def solution(n, times):
    # 1) 답의 범위를 잡는다: 최소 1분, 최대 (가장 느린 심사관) * n분
    lo, hi = 1, max(times) * n
    # 2) 이진 탐색: T분 안에 n명을 모두 심사할 수 있으면 hi를, 아니면 lo를 좁힌다
    while lo < hi:
        mid = (lo + hi) // 2
        # 3) T분 동안 각 심사관이 처리할 수 있는 사람 수의 합 (n에 도달하면 조기 종료)
        count = 0
        for t in times:
            count += mid // t
            if count >= n:
                break
        if count >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo

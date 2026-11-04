# 프로그래머스 42884 단속카메라
# https://school.programmers.co.kr/learn/courses/30/lessons/42884
# 풀이 날짜: 2026-11-04


def solution(routes):
    # 1. 진출 지점 오름차순으로 정렬 — 카메라 위치의 기준이 된다
    routes.sort(key=lambda r: r[1])

    count = 0
    camera = None  # 2. 가장 최근에 설치한 카메라의 위치
    for start, end in routes:
        # 3. 기존 카메라가 이 차량의 구간을 커버하지 못하면
        #    이 차량의 진출 지점에 새 카메라를 설치한다
        if camera is None or not (start <= camera <= end):
            camera = end
            count += 1
    return count

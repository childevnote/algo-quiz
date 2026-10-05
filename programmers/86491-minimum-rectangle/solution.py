# 프로그래머스 86491 최소직사각형
# https://school.programmers.co.kr/learn/courses/30/lessons/86491
# 2026-10-05

def solution(sizes):
    max_w = 0
    max_h = 0
    for w, h in sizes:
        # 1. 각 명함을 회전시켜 긴 쪽을 가로로 눕히기
        w, h = max(w, h), min(w, h)
        # 2. 지금까지 본 명함 중 가장 긴 가로/세로 갱신
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    # 3. 가장 작은 지갑의 크기
    return max_w * max_h

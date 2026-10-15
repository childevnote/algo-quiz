# https://school.programmers.co.kr/learn/courses/30/lessons/12906
# solved: 2026-10-15
def solution(arr):
    result = []
    for x in arr:
        # 1. 결과 리스트의 마지막 값과 현재 값이 다를 때만 추가 (연속 중복 제거)
        if not result or result[-1] != x:
            result.append(x)
    return result

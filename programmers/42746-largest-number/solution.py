# https://school.programmers.co.kr/learn/courses/30/lessons/42746
# 프로그래머스 42746 - 가장 큰 수 (Lv.2, 정렬)
# 작성일: 2026-10-19 (18:00 자동 풀이)

from functools import cmp_to_key


def solution(numbers):
    # 1. 숫자를 문자열로 변환 (이어 붙이기 비교를 위해)
    strs = [str(n) for n in numbers]
    # 2. (a+b)와 (b+a) 중 더 큰 쪽을 앞에 오게 정렬
    strs.sort(key=cmp_to_key(lambda a, b: -1 if a + b > b + a else 1))
    # 3. 모두 0인 경우 "0"을 반환 (000... 방지)
    if strs[0] == "0":
        return "0"
    # 4. 이어 붙여 반환
    return "".join(strs)

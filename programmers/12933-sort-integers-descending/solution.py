# 프로그래머스 12933 - 정수 내림차순으로 배치하기
# https://school.programmers.co.kr/learn/courses/30/lessons/12933
# 풀이 날짜: 2026-11-26

def solution(n):
    # 1. n을 문자열로 바꿔 각 자릿수를 문자로 만든다.
    # 2. 자릿수 문자를 내림차순으로 정렬한다.
    # 3. 이어 붙인 뒤 정수로 되돌린다.
    return int("".join(sorted(str(n), reverse=True)))

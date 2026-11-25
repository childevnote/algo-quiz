# 프로그래머스 12932 - 자연수 뒤집어 배열로 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12932
# 풀이 날짜: 2026-11-25

def solution(n):
    # 1. 10으로 나눈 나머지가 일의 자리 숫자이다.
    # 2. 나머지를 순서대로 모으면 뒤집힌 자릿수 배열이 된다.
    # 3. 10으로 나눈 몫으로 자리수를 한 칸씩 줄여 나간다.
    answer = []
    while n > 0:
        answer.append(n % 10)
        n //= 10
    return answer

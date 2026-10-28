# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42885
# 풀이 날짜: 2026-10-28
# 구명보트 (Lv.2, 탐욕법)


def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    while left <= right:
        # 1. 가장 가벼운 사람과 가장 무거운 사람을 한 배에 태울 수 있으면 함께 태운다
        if people[left] + people[right] <= limit:
            left += 1
        # 2. 가장 무거운 사람은 어느 경우든 이번 배에 태운다 (혼자 타거나, 짝과 함께)
        right -= 1
        boats += 1
    return boats

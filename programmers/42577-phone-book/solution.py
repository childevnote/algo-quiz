# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/42577
# 풀이일: 2026-10-08
# Lv.2 · 해시 — 전화번호 목록

def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        # ① 정렬 후에는 인접한 두 원소만 비교하면 된다
        if phone_book[i + 1].startswith(phone_book[i]):
            return False
    return True

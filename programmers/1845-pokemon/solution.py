# https://school.programmers.co.kr/learn/courses/30/lessons/1845
# 폰켓몬 — 풀이일: 2026-10-14

def solution(nums):
    pick = len(nums) // 2
    kinds = len(set(nums))
    return min(pick, kinds)

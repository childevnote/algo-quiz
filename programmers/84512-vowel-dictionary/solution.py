# 프로그래머스 84512 - 모음사전
# https://school.programmers.co.kr/learn/courses/30/lessons/84512
# 풀이일: 2026-10-25

def solution(word):
    vowels = "AEIOU"
    # 1. 자기 자신과 조상 단어 수만큼 기본 카운트 (길이만큼)
    answer = len(word)
    for i, ch in enumerate(word):
        # 2. 현재 자리보다 작은 모음 개수
        idx = vowels.index(ch)
        # 3. 그 모음 아래에 달린 서브트리 단어 수: 1 + 5 + ... + 5^(4-i)
        subtree = (5 ** (5 - i) - 1) // 4
        # 4. 건너뛴 서브트리만큼 더한다
        answer += idx * subtree
    return answer

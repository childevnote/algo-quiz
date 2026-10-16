# 프로그래머스 42840 모의고사 (https://school.programmers.co.kr/learn/courses/30/lessons/42840)
# 풀이 날짜: 2026-10-16

def solution(answers):
    # ① 각 수포자의 찍기 패턴 (반복 주기)
    patterns = [
        [1, 2, 3, 4, 5],                  # 1번: 길이 5
        [2, 1, 2, 3, 2, 4, 2, 5],         # 2번: 길이 8
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5],   # 3번: 길이 10
    ]

    # ② 각 패턴을 answers 길이에 맞춰 순환하며 맞힌 개수 세기
    scores = []
    for p in patterns:
        m = len(p)
        score = sum(1 for i, a in enumerate(answers) if a == p[i % m])
        scores.append(score)

    # ③ 최고점과 동점자를 찾아 오름차순 반환
    best = max(scores) if scores else 0
    return [i + 1 for i, s in enumerate(scores) if s == best]

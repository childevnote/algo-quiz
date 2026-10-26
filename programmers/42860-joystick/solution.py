# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42860
# 풀이 날짜: 2026-10-26

def solution(name):
    # 1. 상하 조작: 각 자리마다 A에서 목표 문자까지 위/아래 중 짧은 쪽
    answer = 0
    for ch in name:
        up = ord(ch) - ord('A')
        answer += min(up, 26 - up)

    # 2. 좌우 이동: 기본은 오른쪽으로 끝까지 가는 n-1회.
    #    연속된 'A' 구간을 만나면, 되돌아가거나 왼쪽으로 먼저 돌아
    #    그 구간을 건너뛰는 편이 짧아질 수 있어 두 방향 모두 계산한다.
    n = len(name)
    move = n - 1
    for i in range(n):
        nxt = i + 1
        while nxt < n and name[nxt] == 'A':
            nxt += 1
        # i까지 갔다가 되돌아와 반대쪽에서 nxt로 진입 / 왼쪽으로 먼저 돌아 반대쪽에서 진입
        move = min(move, i * 2 + n - nxt, (n - nxt) * 2 + i)
    return answer + move

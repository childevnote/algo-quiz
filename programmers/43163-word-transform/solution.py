# 단어 변환 (프로그래머스 43163)
# https://school.programmers.co.kr/learn/courses/30/lessons/43163
# 2026-11-09
from collections import deque


def solution(begin, target, words):
    word_set = set(words)
    # 1. target이 words에 없으면 변환 자체가 불가능하다.
    if target not in word_set:
        return 0

    # 2. BFS: 큐에 (단어, 지금까지의 단계 수)를 넣고 한 글자씩 바꿔가며 탐색한다.
    queue = deque([(begin, 0)])
    visited = {begin}
    length = len(begin)

    while queue:
        word, steps = queue.popleft()
        # 3. target에 도달하면 그때의 단계 수가 최단 변환 횟수이다.
        if word == target:
            return steps
        # 4. 각 자리마다 26개 알파벳으로 바꿔본 뒤 words 안에 있는 단어만 다음 후보로 삼는다.
        for i in range(length):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if ch == word[i]:
                    continue
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in word_set and nxt not in visited:
                    visited.add(nxt)
                    queue.append((nxt, steps + 1))

    # 5. 큐를 다 비워도 target에 닿지 못하면 변환 불가.
    return 0

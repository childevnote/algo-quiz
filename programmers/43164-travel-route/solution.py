# 여행경로 (프로그래머스 43164)
# https://school.programmers.co.kr/learn/courses/30/lessons/43164
# 2026-11-11
from collections import defaultdict


def solution(tickets):
    graph = defaultdict(list)
    # 1. 출발 공항별로 도착 공항 목록을 만든다.
    for src, dst in tickets:
        graph[src].append(dst)
    # 2. 알파벳 역순으로 정렬해 두면 pop()으로 가장 작은 도착 공항을 꺼낼 수 있다.
    for dsts in graph.values():
        dsts.sort(reverse=True)

    route = []
    stack = ["ICN"]
    # 3. Hierholzer 알고리즘: 더 이상 갈 간선이 없을 때만 경로에 확정한다.
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop())
        route.append(stack.pop())
    # 4. 확정 순서가 역순이므로 뒤집으면 ICN에서 시작하는 전체 경로가 된다.
    return route[::-1]

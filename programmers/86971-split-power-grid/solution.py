# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/86971
# 풀이 날짜: 2026-10-24
# 전력망을 둘로 나누기 (Lv.2, 완전탐색)

def solution(n, wires):
    # 1. 인접 리스트 구성 (노드 번호 1..n)
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    # 2. 1번 노드를 루트로 하는 반복 DFS로 부모·방문 순서 기록
    parent = [0] * (n + 1)
    order = []
    stack = [1]
    parent[1] = -1
    while stack:
        node = stack.pop()
        order.append(node)
        for nxt in graph[node]:
            if nxt != parent[node] and parent[nxt] == 0:
                parent[nxt] = node
                stack.append(nxt)

    # 3. 역순으로 서브트리 크기 누적 (자식 크기를 부모에 합산)
    size = [1] * (n + 1)
    for node in reversed(order):
        if parent[node] > 0:
            size[parent[node]] += size[node]

    # 4. 각 간선(부모-자식)을 끊었을 때 차이 = |n - 2 * 서브트리 크기|
    return min(abs(n - 2 * size[node]) for node in range(2, n + 1))

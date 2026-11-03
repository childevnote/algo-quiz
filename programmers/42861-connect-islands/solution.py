# 프로그래머스 42861 섬 연결하기
# 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42861
# 풀이 날짜: 2026-11-03


def solution(n, costs):
    # 1. 간선을 비용 오름차순으로 정렬
    costs.sort(key=lambda x: x[2])

    parent = list(range(n))  # 2. 각 섬의 집합 대표 (자기 자신으로 초기화)

    def find(x):
        # 3. 경로 압축을 적용한 find
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    total = 0
    used = 0
    for a, b, c in costs:
        ra, rb = find(a), find(b)
        # 4. 두 섬이 다른 집합이면 간선 선택 (사이클 방지)
        if ra != rb:
            parent[rb] = ra
            total += c
            used += 1
            # 5. n-1개 간선을 고르면 최소 신장 트리 완성
            if used == n - 1:
                break

    return total

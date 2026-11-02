# 이중우선순위큐

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42628
- 레벨: Lv.3
- 카테고리: 힙
- 풀이 날짜: 2026-11-02

## 문제 분석 및 핵심 로직

삽입(I 숫자), 최댓값 삭제(D 1), 최솟값 삭제(D -1) 세 가지 연산을 지원하는 이중 우선순위 큐를 구현하는 문제다. 모든 연산을 처리한 뒤 큐가 비어 있으면 [0, 0], 남아 있으면 [최댓값, 최솟값]을 반환한다. 연산은 최대 1,000,000개까지 주어지므로, 연산마다 전체를 스캔하면 제한을 넘는다.

핵심은 두 가지다.

1. **최댓값과 최솟값을 각각 O(log n)에 꺼낼 수 있어야 한다.** 최소 힙 하나만으로는 최댓값을 꺼낼 수 없고, 최대 힙 하나만으로는 최솟값을 꺼낼 수 없다. 그래서 최소 힙과 최대 힙을 두 개 함께 쓴다.
2. **한쪽 힙에서 삭제한 원소가 다른 쪽 힙에 그대로 남아 있는 문제를 해결해야 한다.** 예를 들어 최댓값을 삭제하면 그 값은 최소 힙에서도 사라져야 하지만, 최소 힙 안에 들어 있는 값을 직접 찾아 지우는 것은 O(n)이 걸린다. 대신 삭제된 값을 표시만 해 두고, 나중에 그 값이 힙의 맨 위에 올라왔을 때 건너뛰는 지연 삭제(lazy deletion)를 쓴다. 살아 있는 개수를 세는 딕셔너리(맵)가 그 표시 역할을 한다.

### 초심자 방식 vs 개선 방식

처음 떠올리기 쉬운 방식은 리스트 하나에 값을 모아 두고, 최댓값·최솟값 삭제 때마다 `max()`/`min()`으로 찾아 `remove()`로 지우는 것이다. 연산 하나에 O(n)이 걸리므로 연산이 100만 개면 10^12 수준이 되어 제한 안에 끝나지 않는다.

정렬된 리스트(예: `bisect`로 삽입 위치를 찾는 방식)를 쓰는 방법도 있다. 최댓값·최솟값 조회는 O(1)이지만, 리스트 중간에 삽입·삭제할 때 뒤 원소들을 전부 밀어야 하므로 여전히 연산마다 O(n)이다.

두 개의 힙과 개수 딕셔너리를 함께 쓰는 방식은 삽입·삭제가 모두 O(log n)이다. 삭제한 값을 즉시 지우지 않고 stale 상태로 남겨 두는 대신, 힙의 맨 위에서 stale 원소를 만날 때만 버린다. stale 원소는 한 번 버려지면 다시 등장하지 않으므로, 건너뛰는 비용을 모두 합쳐도 전체 연산 횟수를 넘지 않는다.

### 동작 원리

1. 최소 힙, 최대 힙(파이썬은 음수를 넣어 최소 힙으로 구현, 자바는 역순 비교자), 그리고 값별 살아 있는 개수를 세는 딕셔너리(맵)를 준비한다.
2. 삽입 연산이 오면 두 힙에 모두 넣고, 딕셔너리의 개수를 1 늘린다.
3. 최댓값 삭제가 오면, 최대 힙의 맨 위가 이미 삭제된 값(stale)인 동안 pop으로 버린다. 맨 위가 살아 있는 값이면 pop하고 개수를 1 줄인다. 힙이 비어 있으면 연산을 무시한다.
4. 최솟값 삭제도 같은 방식으로 최소 힙에서 수행한다.
5. 모든 연산이 끝나면 양쪽 힙의 맨 위를 stale 원소가 없을 때까지 정리한다. 최대 힙이 비어 있으면 큐가 비어 있는 것이므로 [0, 0]을, 남아 있으면 [최댓값, 최솟값]을 반환한다.

중복된 값이 들어 있는 경우에도 개수 딕셔너리가 값을 구분한다. 예를 들어 5를 두 번 삽입하면 개수가 2가 되고, 최댓값 삭제를 한 번 하면 1이 남아 두 번째 5는 여전히 최댓값이자 최솟값으로 조회된다.

## 최종 솔루션 코드

### Python

```python
import heapq


def solution(operations):
    min_heap = []  # 1. 최솟값 꺼내기용 최소 힙
    max_heap = []  # 2. 최댓값 꺼내기용 최대 힙 (음수 저장)
    count = {}     # 3. 값이 실제로 큐에 몇 개 남아 있는지 세는 딕셔너리

    for op in operations:
        cmd, num_str = op.split()
        num = int(num_str)

        if cmd == "I":
            # 삽입: 두 힙 모두에 넣고 개수 기록
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            count[num] = count.get(num, 0) + 1
        elif num == 1:
            # 4. 최댓값 삭제: 이미 삭제된 stale 원소를 건너뛰고 pop
            while max_heap and count.get(-max_heap[0], 0) == 0:
                heapq.heappop(max_heap)
            if max_heap:
                count[-heapq.heappop(max_heap)] -= 1
        else:  # num == -1
            # 5. 최솟값 삭제: 같은 방식으로 최소 힙에서 pop
            while min_heap and count.get(min_heap[0], 0) == 0:
                heapq.heappop(min_heap)
            if min_heap:
                count[heapq.heappop(min_heap)] -= 1

    # 6. 양쪽 힙의 top을 stale 원소 없이 정리
    while max_heap and count.get(-max_heap[0], 0) == 0:
        heapq.heappop(max_heap)
    while min_heap and count.get(min_heap[0], 0) == 0:
        heapq.heappop(min_heap)

    if not max_heap:
        return [0, 0]
    return [-max_heap[0], min_heap[0]]
```

### Java

```java
import java.util.HashMap;
import java.util.Map;
import java.util.PriorityQueue;

class Solution {
    public int[] solution(String[] operations) {
        PriorityQueue<Integer> minHeap = new PriorityQueue<>();  // 1. 최솟값 꺼내기용 최소 힙
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(java.util.Comparator.reverseOrder());  // 2. 최댓값 꺼내기용 최대 힙
        Map<Integer, Integer> count = new HashMap<>();  // 3. 값이 실제로 큐에 몇 개 남아 있는지 세는 맵

        for (String op : operations) {
            String[] parts = op.split(" ");
            int num = Integer.parseInt(parts[1]);

            if (parts[0].equals("I")) {
                // 삽입: 두 힙 모두에 넣고 개수 기록
                minHeap.offer(num);
                maxHeap.offer(num);
                count.put(num, count.getOrDefault(num, 0) + 1);
            } else if (num == 1) {
                // 4. 최댓값 삭제: 이미 삭제된 stale 원소를 건너뛰고 poll
                while (!maxHeap.isEmpty() && count.getOrDefault(maxHeap.peek(), 0) == 0) {
                    maxHeap.poll();
                }
                if (!maxHeap.isEmpty()) {
                    int v = maxHeap.poll();
                    count.put(v, count.get(v) - 1);
                }
            } else {  // num == -1
                // 5. 최솟값 삭제: 같은 방식으로 최소 힙에서 poll
                while (!minHeap.isEmpty() && count.getOrDefault(minHeap.peek(), 0) == 0) {
                    minHeap.poll();
                }
                if (!minHeap.isEmpty()) {
                    int v = minHeap.poll();
                    count.put(v, count.get(v) - 1);
                }
            }
        }

        // 6. 양쪽 힙의 top을 stale 원소 없이 정리
        while (!maxHeap.isEmpty() && count.getOrDefault(maxHeap.peek(), 0) == 0) {
            maxHeap.poll();
        }
        while (!minHeap.isEmpty() && count.getOrDefault(minHeap.peek(), 0) == 0) {
            minHeap.poll();
        }

        if (maxHeap.isEmpty()) {
            return new int[]{0, 0};
        }
        return new int[]{maxHeap.peek(), minHeap.peek()};
    }
}
```

## 학습 노트

- 막혔던 점: 18:00 자동 풀이로 진행되어 별도의 막힘 없이 풀이했다. 주의할 점은 한쪽 힙에서 삭제한 값이 다른 쪽 힙에 그대로 남아 있다는 것으로, 삭제 즉시 양쪽을 동기화하려 하면 O(n)이 되므로 지연 삭제로 미뤄야 한다는 점이다.
- 핵심 포인트: 최소 힙과 최대 힙을 함께 쓰고, 값별 살아 있는 개수를 세는 딕셔너리(맵)로 stale 원소를 판정하는 지연 삭제다. 힙의 맨 위에서만 stale 검사를 하면 전체 비용이 O(n log n)으로 유지된다.
- 개선: 전체 스캔(O(n))이나 정렬 리스트 삽입(O(n)) 대신 힙 삽입·추출(O(log n))을 사용했고, 중복 값은 개수 딕셔너리로 구분해 같은 값을 여러 번 삽입·삭제해도 정확히 동작한다.

## 성능 측정

로컬 실측 (2026-11-02, n=100,000 무작위 케이스: 삽입 60%·최댓값 삭제 20%·최솟값 삭제 20%, 값 범위 -10,000~10,000, 시드 42; 언어별로 난수 생성기가 달라 데이터셋이 다름).

| 케이스 | Python | Java |
| --- | --- | --- |
| 입출력 예 1 ([0, 0]) | 0.029 ms | 0.806 ms (첫 호출, 클래스 로딩 포함) |
| 입출력 예 2 ([333, -45]) | 0.016 ms | 0.210 ms |
| n=100,000 무작위 | 0.312 s | 0.252 s |
| n=100,000 피크 메모리 (Python, tracemalloc) | 약 3.7 MiB | — |

- 시간 복잡도: O(n log n) — 연산마다 힙 삽입·추출 O(log n), stale 원소 건너뛰기는 각 원소당 최대 한 번이라 전체 상각 O(n log n)
- 공간 복잡도: O(n) — 두 개의 힙과 개수 딕셔너리

## 요약

- 최댓값과 최솟값을 모두 O(log n)에 꺼내야 하는 이중 우선순위 큐 문제다.
- 최소 힙과 최대 힙을 함께 쓰고, 삭제한 값은 개수 딕셔너리(맵)로 표시만 해 두는 지연 삭제로 양쪽 힙의 동기화 문제를 해결한다.
- 힙의 맨 위에서 stale 원소를 만날 때만 버리면, 삭제 비용이 전체 연산 횟수를 넘지 않는다.
- 빈 큐에서의 삭제 연산은 무시하고, 마지막에 큐가 비어 있으면 [0, 0]을 반환한다.

# 개념: 힙(Heap)

## 힙이란

힙은 **완전 이진 트리** 형태를 유지하면서, 부모 노드가 항상 자식 노드보다 우선순위가 높은(최소 힙이면 작거나 같은, 최대 힙이면 크거나 같은) 자료구조다. 우선순위 큐를 구현하는 가장 일반적인 방법이다.

힙의 핵심 보장은 딱 하나다: **가장 우선순위가 높은 원소를 상수 시간에 확인하고, 로그 시간에 꺼낼 수 있다.** 트리 전체가 정렬되어 있지는 않다. 루트(배열의 0번 인덱스)만 최소(또는 최대)임이 보장될 뿐, 나머지는 부분 순서만 지킨다.

## 연산과 비용

| 연산 | 내용 | 시간 복잡도 |
|---|---|---|
| heapify | 배열 전체를 힙으로 변환 | O(n) |
| push (삽입) | 말단에 추가 후 위로 올림 | O(log n) |
| pop (추출) | 루트를 꺼내고 말단을 루트로 옮긴 뒤 아래로 내림 | O(log n) |
| peek | 루트 확인 | O(1) |

정렬된 리스트를 매번 다시 정렬하는 O(n log n) 반복과 비교하면, 힙은 "최소값만 계속 꺼내고 넣는" 작업에 특화되어 있다. 꺼내고 넣는 횟수가 많을수록 차이가 벌어진다.

## 최소 힙 vs 최대 힙

- 최소 힙: 루트가 가장 작다. "가장 작은 것을 반복해서 처리"할 때 사용한다.
- 최대 힙: 루트가 가장 크다. "가장 큰 것을 반복해서 처리"할 때 사용한다.

Python의 `heapq`는 최소 힙만 제공한다. 최대 힙이 필요하면 부호를 뒤집어 넣는 관례를 쓴다.

## 일반적인 예시

```python
import heapq

h = []
heapq.heappush(h, 5)
heapq.heappush(h, 1)
heapq.heappush(h, 3)
print(h[0])        # 1 — 루트 확인은 O(1)
print(heapq.heappop(h))  # 1 — 가장 작은 값 추출
print(heapq.heappop(h))  # 3
```

배열 전체를 한 번에 힙으로 만들 때는 `heapify`가 push 반복보다 빠르다:

```python
data = [5, 1, 3, 4, 2]
heapq.heapify(data)  # O(n)
```

Java에서는 `PriorityQueue`가 힙 기반 우선순위 큐다:

```java
import java.util.PriorityQueue;

PriorityQueue<Integer> pq = new PriorityQueue<>();  // 최소 힙
pq.offer(5);
pq.offer(1);
System.out.println(pq.peek());  // 1
System.out.println(pq.poll());  // 1
```

## 언제 힙을 떠올릴까

"매번 전체 중 가장 작은(또는 가장 큰) 것을 꺼내서 무언가 하고 다시 넣는다"는 패턴이 보이면 힙이 1순위 후보다. 이 패턴에서 정렬 반복은 거의 항상 시간 초과를 부른다.

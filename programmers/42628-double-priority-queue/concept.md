# 개념 정리: 이중우선순위큐

## 1. 최소 힙과 최대 힙 (Min-Heap / Max-Heap)

힙은 가장 작거나(최소 힙) 가장 큰(최대 힙) 원소를 항상 루트에 두는 이진 트리 기반 자료구조다. 삽입과 삭제가 모두 O(log n)이며, "지금까지 본 것 중 가장 작은(또는 큰) 것"을 반복해서 꺼내야 할 때 쓴다.

- 최소 힙에서는 부모가 자식보다 항상 작거나 같다. 루트를 꺼내면 다음으로 작은 원소가 루트로 올라온다. 최대 힙은 부호만 반대다.
- 정렬된 리스트와 달리 힙은 전체를 정렬하지 않는다. 가장 작은 원소만 필요할 때 정렬보다 저렴하다. 전체 정렬은 O(n log n)이지만 힙에서 원소 하나를 꺼내는 것은 O(log n)이다.
- 파이썬에서는 `heapq` 모듈이 리스트를 최소 힙으로 다룬다. `heapq.heappush(heap, x)`로 삽입하고 `heapq.heappop(heap)`으로 가장 작은 원소를 꺼낸다. 최대 힙이 필요하면 부호를 뒤집어 저장한다.
- 자바에서는 `PriorityQueue`가 최소 힙이다. `offer`로 삽입하고 `poll`로 가장 작은 원소를 꺼낸다. 최대 힙은 `Comparator.reverseOrder()`를 생성자에 넘겨 만든다.

```python
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
print(heapq.heappop(heap))  # 1 — 가장 작은 원소가 먼저 나온다

max_heap = []
heapq.heappush(max_heap, -3)
heapq.heappush(max_heap, -1)
print(-heapq.heappop(max_heap))  # 3 — 부호를 뒤집으면 최대 힙처럼 동작한다
```

```java
import java.util.*;

PriorityQueue<Integer> minHeap = new PriorityQueue<>();
minHeap.offer(3);
minHeap.offer(1);
System.out.println(minHeap.poll());  // 1

PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Comparator.reverseOrder());
maxHeap.offer(3);
maxHeap.offer(1);
System.out.println(maxHeap.poll());  // 3
```

### 한 자료구조로는 양쪽 극단을 못 꺼낸다

최소 힙은 최솟값만, 최대 힙은 최댓값만 O(log n)에 꺼낼 수 있다. 반대쪽 극단은 힙 내부 어딘가에 흩어져 있어 찾으려면 전체를 뒤져야 한다. 최댓값과 최솟값을 둘 다 자주 꺼내야 한다면, 최소 힙과 최대 힙을 함께 유지하는 것이 자연스러운 출발점이다. 다만 두 힙에 같은 값을 중복해서 넣게 되므로, 한쪽에서 삭제한 값을 다른 쪽에서 어떻게 처리할지가 다음 문제다.

## 2. 지연 삭제 (Lazy Deletion)

힙에서 임의의 원소를 직접 찾아 지우는 것은 O(n)이 걸린다. 힙은 루트만 빠르게 꺼낼 수 있고, 중간 원소의 위치를 모르기 때문이다. 지연 삭제는 삭제를 "표시만 해 두고 실제 제거는 나중으로 미루는" 기법이다.

- 삭제하고 싶은 원소가 있으면, 별도의 딕셔너리나 집합에 "이 원소는 삭제됐다"는 표시를 남긴다. 힙 안의 원소는 그대로 둔다.
- 힙의 맨 위(top)를 볼 때마다 표시를 확인한다. 표시된 원소면 pop으로 버리고 다음 원소를 본다. 살아 있는 원소가 맨 위에 올라올 때까지 반복한다.
- stale 원소는 한 번 버려지면 다시 등장하지 않으므로, 건너뛰는 작업 전체를 합쳐도 삽입된 원소 수를 넘지 않는다. 그래서 전체 시간 복잡도는 그대로 O(n log n)으로 유지된다.
- 삭제 표시를 저장하는 방식은 상황에 따라 다르다. 같은 값이 여러 번 들어갈 수 있다면 값별 개수를 세는 딕셔너리(맵)를 쓰고, 각 원소가 고유하다면 삭제된 원소의 식별자를 집합에 넣는다.

```python
import heapq

heap = []
count = {}  # 값별 살아 있는 개수

def insert(x):
    heapq.heappush(heap, x)
    count[x] = count.get(x, 0) + 1

def delete_min():
    while heap and count.get(heap[0], 0) == 0:  # stale 원소 건너뛰기
        heapq.heappop(heap)
    if heap:
        count[heapq.heappop(heap)] -= 1

insert(5)
insert(3)
insert(5)
delete_min()  # 3 삭제
print(heap)   # [5, 5] — 3은 이미 나갔고, 5 두 개가 남아 있다
```

### 왜 맨 위에서만 검사하는가

힙의 성질상 맨 위가 아닌 원소는 아직 꺼낼 차례가 아니다. 그 원소가 stale인지 확인하는 것은 그 원소가 맨 위에 올라왔을 때로 미뤄도 답에 영향을 주지 않는다. 이 "필요할 때까지 미룬다"는 점이 지연 삭제의 핵심이다. 반대로 힙 안을 전부 정리하려 들면 매번 O(n)이 들어 지연 삭제의 이득이 사라진다.

## 3. 두 개의 힙으로 양쪽 극단 유지하기

최솟값과 최댓값을 모두 지원해야 할 때, 최소 힙과 최대 힙을 나란히 두고 같은 값을 양쪽에 삽입하는 패턴이다. 삭제는 한쪽 힙에서만 일어나고, 다른 쪽 힙에는 stale 원소로 남는다. 개수 딕셔너리가 두 힙 사이의 유일한 동기화 수단이 된다.

- 삽입: 두 힙에 모두 넣고 개수를 1 늘린다.
- 최댓값 삭제: 최대 힙의 맨 위부터 stale 원소를 버린 뒤, 살아 있는 최댓값을 pop하고 개수를 1 줄인다. 최소 힙은 건드리지 않는다.
- 최솟값 삭제: 최소 힙에서 같은 과정을 수행한다.
- 조회: 양쪽 힙의 맨 위를 stale 원소 없이 정리한 뒤, 최대 힙의 top이 최댓값, 최소 힙의 top이 최솟값이다.

이 패턴은 "양쪽 극단을 모두 조회하는 자료구조"가 필요할 때 반복해서 등장한다. 예를 들어 슬라이딩 윈도우에서 구간의 최댓값과 최솟값을 동시에 묻는 문제, 양쪽에서 원소를 빼는 덱 형태의 우선순위 큐 등이 같은 구조로 풀린다.

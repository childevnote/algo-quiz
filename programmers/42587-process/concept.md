# 프로세스를 푸는 데 필요한 개념

## 1. 큐 (Queue)

큐는 먼저 들어온 원소가 먼저 나가는(FIFO, First-In-First-Out) 선형 자료구조다. `enqueue`(뒤에 삽입)와 `dequeue`(앞에서 제거)가 기본 연산이며 둘 다 O(1)이다.

```python
from collections import deque

q = deque()
q.append(1)    # enqueue
q.append(2)
q.popleft()    # dequeue -> 1
```

리스트로 `pop(0)`을 사용하면 뒤 원소들을 전부 한 칸씩 당기므로 O(n)이 걸린다. 앞뒤 연산이 잦을 때는 `deque`를 쓴다.

```java
import java.util.ArrayDeque;
import java.util.Queue;

Queue<Integer> q = new ArrayDeque<>();
q.offer(1);   // enqueue
q.offer(2);
q.poll();     // dequeue -> 1
```

Java의 `ArrayDeque`는 양 끝 삽입/삭제가 상각 O(1)이다. `LinkedList`도 `Queue` 인터페이스를 제공하지만 노드 기반이라 캐시 효율이 떨어져 `ArrayDeque`가 일반적으로 빠르다.

## 2. 시뮬레이션

시뮬레이션은 문제의 규칙을 그대로 코드로 옮겨 상태를 한 단계씩 갱신해 나가는 접근법이다. 수식이나 탐색으로 닫힌 형태의 해를 구하기 어려울 때 사용한다.

일반적인 골격:

```python
while not 종료조건:
    상태를 관찰하고
    규칙에 따라 상태를 갱신한다
```

큐에 "조건을 만족하지 않으면 뒤로 보낸다"는 규칙이 붙으면 실행 순서가 입력 순서와 달라지므로, 시뮬레이션으로 실제 순서를 재현하는 것이 가장 직관적이다.

## 3. 빈도표 (Frequency Table / Counting)

값의 범위가 고정되어 있고 좁을 때, 각 값이 몇 개 나타나는지를 배열에 세어 두는 기법이다. "현재 남은 최대값은 얼마인가" 같은 질의를 O(1)에 처리할 수 있다.

```python
# 값이 1~9 사이로 고정되어 있을 때
freq = [0] * 10
for v in values:
    freq[v] += 1

highest = 9
while freq[highest] == 0:
    highest -= 1
# highest: 남은 값 중 최대
```

값을 하나 소비하면 해당 칸을 1 감소시키고, 칸이 0이 되면 최대값을 한 칸씩 내리며 다음으로 큰 값이 남은 칸을 찾는다. 값의 종류가 k개로 고정되어 있으면 최대값 갱신은 O(k) 상수 시간이다. 이 원리는 계수 정렬(counting sort)과 같다.

## 4. 시간 복잡도 비교 — 매번 스캔 vs 빈도표

n개의 원소에 대해 "남은 원소 중 최대값이 있는가"를 매번 판단한다고 하자.

- 매번 스캔: 한 번 판단에 O(n), 전체 최대 O(n²). 판단 횟수가 n에 비례하기 때문이다.
- 빈도표: 한 번 판단에 O(1), 전체 O(n). 최대값 갱신 비용이 값 종류 수 k에 묶여 상수로 취급된다.

n이 작으면 차이가 미미하지만 n이 커지면 격차가 벌어진다. "값의 범위가 제한되어 있다"는 조건은 빈도표를 쓸 수 있다는 신호다.

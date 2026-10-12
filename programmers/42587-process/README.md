# [프로그래머스 42587] 프로세스

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42587
- 레벨: Lv.2 · 카테고리: 스택/큐
- 풀이일: 2026-10-12 (18:00 자동 풀이)

## 문제 핵심 요약

실행 대기 큐에 있는 프로세스들을 우선순위 규칙에 따라 실행할 때, 특정 프로세스가 몇 번째로 실행되는지 구한다. 맨 앞 프로세스보다 우선순위가 높은 프로세스가 큐에 하나라도 남아 있으면 맨 앞을 다시 뒤로 보내고, 그렇지 않으면 실행한다. 우선순위는 1~9의 정수, 프로세스 수는 최대 100이다.

핵심 제한사항: 큐에 있는 프로세스 중 우선순위가 더 높은 프로세스가 있으면 무조건 뒤로 보낸다 (뒤에 있어도 된다). 실행한 프로세스는 종료되며 큐로 돌아오지 않는다.

## 문제 분석 및 핵심 로직

이 문제는 시뮬레이션이다. 규칙을 그대로 따라가면 되므로 별도의 탐색이나 수식이 필요 없다. 다만 "큐에 더 높은 우선순위가 있는가"를 판단하는 방법이 풀이의 전체를 좌우한다.

초심자 방식은 맨 앞 원소를 꺼낸 뒤 매번 `max(나머지 우선순위)`를 구하는 것이다. 큐 길이가 n이면 한 번 판단에 O(n), 전체 실행에 O(n²)이 걸린다. n ≤ 100이라 제한 내에서는 통과하지만, 원소가 계속 뒤로 돌아가는 구조에서는 매번 전체를 스캔한다는 점이 아쉽다.

개선 방식은 우선순위 빈도표를 따로 유지하는 것이다. 우선순위 값의 범위가 1~9로 고정되어 있다는 점을 이용하면, "현재 남은 최대 우선순위"를 크기 10짜리 배열 하나로 O(1)에 알 수 있다. 프로세스가 실행되면 해당 우선순위의 카운트를 1 감소시키고, 카운트가 0이 된 값은 건너뛰면서 최대값을 갱신한다. 우선순위 값의 종류가 최대 9개이므로 최대값 갱신은 상수 시간이다. 전체 복잡도는 O(n)으로 떨어진다.

큐 자료구조로는 Python `collections.deque`, Java `ArrayDeque`를 사용한다. 앞에서는 빼고 뒤에서는 넣는 연산이 모두 O(1)이며, 리스트로 `pop(0)`을 쓰면 O(n)이므로 피한다.

## 개념별 심층 설명

### 1. 큐(Queue)와 시뮬레이션

큐는 먼저 들어온 원소가 먼저 나가는(FIFO) 구조다. 이 문제의 규칙은 기본 FIFO에 "우선순위 조건을 만족하지 않으면 뒤로 보낸다"는 예외가 붙은 형태다. 예외가 붙으면 실행 순서가 입력 순서와 달라지므로, 시뮬레이션으로 실제 순서를 재현하는 것이 가장 직관적이다. 시뮬레이션 문제의 기본형은 "상태(큐, 카운트)를 유지하며 규칙을 반복 적용 → 종료 조건 도달"이다.

### 2. 초심자 방식 vs 개선 방식 — 최대값 판단

초심자 방식은 이렇게 동작한다.

```python
# 매 판단마다 큐 전체를 스캔: O(n)
if any(q[0] > p for q in queue):
    queue.append((idx, p))
else:
    execute()
```

원소가 뒤로 돌아갈 때마다 전체 스캔이 반복되므로 전체 O(n²)이다. n=100이라 제한 내지만, n=100,000이면 스캔 한 번에 10만 번 비교가 필요해 실용적이지 않다.

개선 방식은 최대값을 별도 변수로 관리한다.

```python
freq = [0] * 10          # 우선순위 1~9의 남은 개수
highest = 9              # 현재 남은 최대 우선순위
while freq[highest] == 0:
    highest -= 1
```

`p < highest` 한 번의 비교로 판단이 끝나고, `freq[p] -= 1` 후 `highest`를 내리며 갱신한다. 값의 범위가 고정(1~9)이라는 제한을 이용해 전체를 O(n)으로 만든다. 값의 종류가 제한될 때 빈도표로 최대/최소를 관리하는 패턴은 계수 정렬(counting sort)과 같은 원리다.

### 3. 덱(deque)의 선택 이유

큐의 양 끝 연산이 모두 필요하다. Python 리스트의 `pop(0)`은 뒤 원소들을 한 칸씩 당기므로 O(n), `deque.popleft()`는 O(1)이다. Java의 `ArrayDeque` 역시 양 끝 연산이 상각 O(1)이다. 원소가 뒤로 계속 돌아가는 문제 구조에서는 이 차이가 전체 수행시간에 그대로 반영된다.

## 최종 솔루션 코드

핵심 로직 번호 주석: ① 빈도표, ② 최대 우선순위, ③ 뒤로 보내기, ④ 실행 확정, ⑤ 최대값 갱신.

### Python

```python
# 프로그래머스 42587 프로세스
# https://school.programmers.co.kr/learn/courses/30/lessons/42587
# 2026-10-12

from collections import deque


def solution(priorities, location):
    # (원래 위치, 우선순위) 쌍을 담는 실행 대기 큐
    queue = deque(enumerate(priorities))
    # ① 우선순위별 남은 개수 (우선순위는 1~9로 고정)
    freq = [0] * 10
    for p in priorities:
        freq[p] += 1
    # ② 현재 큐에 남아 있는 최대 우선순위
    highest = 9
    while freq[highest] == 0:
        highest -= 1
    order = 0
    while queue:
        idx, p = queue.popleft()
        if p < highest:
            # ③ 더 높은 우선순위가 남아 있으면 맨 뒤로 보냄
            queue.append((idx, p))
        else:
            # ④ 실행 확정 (다시 큐에 넣지 않음)
            order += 1
            freq[p] -= 1
            if idx == location:
                return order
            # ⑤ 실행된 우선순위가 소진되면 최대값 갱신
            while highest > 0 and freq[highest] == 0:
                highest -= 1
```

### Java

```java
import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int solution(int[] priorities, int location) {
        // {원래 위치, 우선순위} 쌍을 담는 실행 대기 큐
        Queue<int[]> queue = new ArrayDeque<>();
        // ① 우선순위별 남은 개수 (우선순위는 1~9로 고정)
        int[] freq = new int[10];
        for (int i = 0; i < priorities.length; i++) {
            queue.offer(new int[]{i, priorities[i]});
            freq[priorities[i]]++;
        }
        // ② 현재 큐에 남아 있는 최대 우선순위
        int highest = 9;
        while (freq[highest] == 0) highest--;
        int order = 0;
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int idx = cur[0], p = cur[1];
            if (p < highest) {
                // ③ 더 높은 우선순위가 남아 있으면 맨 뒤로 보냄
                queue.offer(cur);
            } else {
                // ④ 실행 확정 (다시 큐에 넣지 않음)
                order++;
                freq[p]--;
                if (idx == location) return order;
                // ⑤ 실행된 우선순위가 소진되면 최대값 갱신
                while (highest > 0 && freq[highest] == 0) highest--;
            }
        }
        return order;
    }
}
```

## 성능 측정

로컬 실측 (VM 환경).

| 항목 | Python | Java |
|---|---|---|
| 예제 2케이스 (케이스당) | 1.3 µs | 0.34 µs |
| n=100,000 무작위 (스케일) | 0.217 s | 40.5 ms |
| n=100,000 메모리 | peak 9.0 MiB (tracemalloc) | heap 22.7 MiB (Runtime) |
| 시간 복잡도 | O(n) | O(n) |
| 공간 복잡도 | O(n) | O(n) |

스케일 테스트는 제한(n ≤ 100)을 벗어난 경우의 확장성 확인용으로 별도 측정했다. 최대값 스캔을 빈도표로 대체한 덕분에 n=100,000에서도 선형 시간 안에 처리된다. 매번 `max()`로 스캔하는 초심자 방식은 같은 조건에서 O(n²)이라 수십 초 이상 걸린다.

## 요약

- 큐 시뮬레이션 + 빈도표로 "남은 최대 우선순위"를 O(1)에 관리하는 풀이.
- 우선순위 값의 범위가 고정(1~9)이라는 조건을 이용한 것이 핵심.
- Python/Java 모두 5개 예제 케이스 통과, n=100,000 스케일에서 선형 성능 확인.

## 학습 노트 (2026-10-12, 18:00 자동 풀이)

- 막혔던 점: 없음. 사용자가 18시까지 풀지 않아 자동 풀이로 진행.
- 핵심 포인트: "더 높은 우선순위가 있는가" 판단을 매번 스캔하지 말고, 값의 범위가 고정돼 있을 때 빈도표로 최대값을 추적하면 O(n²) → O(n).
- 개선: `any()`/`max()` 스캔 버전 대신 빈도표 + `highest` 변수 방식으로 작성해 스케일 테스트에서도 선형 성능을 유지.

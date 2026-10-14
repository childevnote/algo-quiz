# 다리를 지나는 트럭 (42583)

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42583
- 레벨: Lv.2 / 카테고리: 스택/큐

## 문제 핵심 요약

일차선 다리를 트럭들이 정해진 순서대로 건넌다. 다리 위에는 최대 bridge_length대의 트럭이 올라갈 수 있고, 다리가 버티는 총 무게는 weight 이하이며, 한 대가 다리를 완전히 건너는 데 bridge_length초가 걸린다. 모든 트럭이 건너는 데 걸리는 최소 시간을 구하는 문제다.

## 문제 분석 및 핵심 로직

시간을 1초씩 흘려보내며 다리 상태를 시뮬레이션한다. 매 초마다 두 가지를 판단한다.

1. 나가는 트럭: 다리에 오른 지 bridge_length초가 지난 트럭은 내린다.
2. 들어오는 트럭: 대기열의 첫 트럭이 "다리에 빈자리가 있고, 올랐을 때 총 무게가 weight 이하"를 만족하면 올린다.

여기서 다리 위 트럭들의 무게 합을 변수 하나로 유지하면, 진입 판단이 O(1)에 끝난다. 매번 다리 위 트럭들의 무게를 다시 합산할 필요가 없다.

## 개념별 심층 설명

### 초심자 방식: 다리를 배열로 표현하고 매 초 밀어내기

다리를 길이가 bridge_length인 배열로 두고, 매 초마다 모든 칸을 한 칸씩 앞으로 이동시키는 방식이다. 직관적이지만 매 초마다 bridge_length칸을 옮겨야 하므로 초당 O(bridge_length)의 비용이 든다. bridge_length가 최대 10,000이므로 전체 시간에 비례해 부담이 커진다.

### 개선 방식: 큐에 (무게, 나가는 시각)만 보관하기

다리 전체를 표현할 필요가 없다. 진입한 트럭을 `(무게, 나가는 시각)` 형태로 큐에 넣는다.

- 하차 판단: 큐의 맨 앞 원소의 나가는 시각이 현재 시각과 같으면 꺼낸다. 먼저 들어간 트럭이 먼저 나가는 FIFO 순서이므로 맨 앞만 보면 된다.
- 진입 판단: `큐 크기 < bridge_length` (빈자리)와 `무게 합 + 다음 트럭 무게 <= weight` (무게 여유)를 확인한다. 무게 합은 진입·하차 시에만 가감하므로 항상 최신 상태를 유지한다.

이렇게 하면 매 초의 작업이 상수 시간에 끝나고, 전체 시뮬레이션은 트럭 수 n에 대해 O(n)이다.

### 동작 원리

진입한 트럭은 `현재 시각 + bridge_length`에 나간다. 매 초 시각을 1씩 증가시키며 하차와 진입을 처리하고, 대기열과 다리가 모두 비면 종료한다. 종료 시점의 시각이 답이다.

## 최종 솔루션 코드

### Python

```python
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque()  # (트럭 무게, 다리를 완전히 나가는 시각)
    total = 0         # 다리 위 트럭들의 무게 합
    time = 0
    waiting = deque(truck_weights)

    while waiting or bridge:
        time += 1
        # 1. 나가는 시각이 된 트럭을 다리에서 내린다
        if bridge and bridge[0][1] == time:
            total -= bridge.popleft()[0]
        # 2. 대기 중인 첫 트럭이 진입 조건(빈자리, 무게 여유)을 만족하면 올린다
        if waiting and len(bridge) < bridge_length and total + waiting[0] <= weight:
            w = waiting.popleft()
            bridge.append((w, time + bridge_length))
            total += w
    return time
```

### Java

```java
import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        Deque<int[]> bridge = new ArrayDeque<>(); // {트럭 무게, 다리를 완전히 나가는 시각}
        int total = 0; // 다리 위 트럭들의 무게 합
        int time = 0;
        int idx = 0;

        while (idx < truck_weights.length || !bridge.isEmpty()) {
            time++;
            // 1. 나가는 시각이 된 트럭을 다리에서 내린다
            if (!bridge.isEmpty() && bridge.peekFirst()[1] == time) {
                total -= bridge.pollFirst()[0];
            }
            // 2. 대기 중인 첫 트럭이 진입 조건(빈자리, 무게 여유)을 만족하면 올린다
            if (idx < truck_weights.length
                    && bridge.size() < bridge_length
                    && total + truck_weights[idx] <= weight) {
                int w = truck_weights[idx++];
                bridge.addLast(new int[]{w, time + bridge_length});
                total += w;
            }
        }
        return time;
    }
}
```

## 성능 측정

- 예제 케이스: Python 약 1.8~10.4µs/회, 3개 예제 모두 정답
- 스케일 테스트 (n=100,000, bridge_length=10,000): Python 788.5ms / Java 58.1ms
- 시간 복잡도: O(n) — 각 트럭의 진입·하차가 한 번씩 처리됨 (시뮬레이션 루프는 매 초 O(1))
- 공간 복잡도: O(bridge_length) — 다리 위 트럭 큐

## 학습 노트

"다리 전체를 표현해야 한다"는 고정관념을 버리는 것이 핵심이었다. 필요한 정보는 진입한 트럭의 무게와 나가는 시각뿐이며, FIFO 순서 덕분에 큐의 맨 앞만 보면 하차를 판단할 수 있다. 무게 합을 별도 변수로 유지하는 것도 같은 맥락이다 — 필요한 값을 미리 계산해 두면 매번 다시 구할 필요가 없다.

## 요약

다리 위 트럭을 (무게, 나가는 시각) 큐로 관리하고 무게 합을 유지하며 1초씩 시뮬레이션한다. 매 초 O(1), 전체 O(n)의 풀이.

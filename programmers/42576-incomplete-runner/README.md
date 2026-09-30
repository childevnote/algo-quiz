# [프로그래머스] 완주하지 못한 선수 Python / Java

https://school.programmers.co.kr/learn/courses/30/lessons/42576
Lv.1 · 해시

## 문제 분석 및 핵심 로직

마라톤 참가자 명단과 완주자 명단을 비교해, 완주하지 못한 한 명의 이름을 찾는 문제다.

**핵심 조건:**

1. **동명이인:** 같은 이름이 여러 번 등장할 수 있다. 존재 여부가 아니라 등장 횟수를 세야 한다.
2. **규모:** 참가자는 최대 100,000명이다. O(n²) 풀이는 시간 초과가 난다.
3. **차이 1명:** 완주자 명단은 참가자보다 정확히 1명 적다. 두 명단의 차집합이 답이다.

## 리스트 순회 방식의 한계

자연스럽게 떠오르는 방법은 완주자 명단을 돌면서 참가자 명단에서 하나씩 지우고, 마지막에 남은 이름을 답으로 삼는 것이다.

```python
for c in completion:
    participant.remove(c)
answer = participant[0]
```

문제는 `list.remove()`의 비용이다. 리스트에서 값을 찾으려면 앞에서부터 순차 탐색을 해야 하므로 한 번의 삭제에 최대 O(n)이 든다. 이를 n번 반복하면 O(n²)이 되고, n이 10만일 경우 100억 번의 비교가 필요해 시간 안에 끝나지 않는다.

## 해시맵을 이용한 O(1) 조회

이럴 때 사용하는 자료구조가 해시맵이다. Python의 `dict`, Java의 `HashMap`이 여기에 해당한다.

### 동작 원리

해시맵은 키를 해시 함수에 통과시켜 얻은 값을 저장 위치로 사용한다.

```
"leo"  → 해시 함수 → 7421번 위치에 저장
"kiki" → 해시 함수 → 309번 위치에 저장
```

조회할 때도 같은 해시 함수를 적용해 해당 위치만 확인하면 되므로, 리스트처럼 전체를 훑을 필요가 없다. 조회·삽입·삭제 모두 평균 O(1)에 동작한다.

## 빈도 세기: Counter

동명이인이 있어 존재 여부가 아니라 횟수를 세야 하므로, `이름 → 등장 횟수` 형태의 집계가 필요하다. Python의 `collections.Counter`는 이 용도에 맞는 도구다.

```python
from collections import Counter

count = Counter(["mislav", "stanko", "mislav", "ana"])
# Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
```

`Counter`는 리스트를 한 번 순회하며 빈도를 집계한다. 여기에 `subtract()`를 활용하면 완주자 명단만큼 차감할 수 있다.

```python
count = Counter(participant)  # 참가자 집계
count.subtract(completion)    # 완주자만큼 차감
# 값이 0보다 큰 이름이 완주하지 못한 사람
```

두 명단을 따로 집계한 뒤 비교하는 대신, 한 번의 차감으로 차집합을 구하는 방식이다.

### 마지막 반복문의 의미

```python
for name, c in count.items():
    if c > 0:
        return name
```

차감 후에는 모든 이름의 값이 0이 되고, 완주하지 못한 한 사람의 값만 1로 남는다. 따라서 값이 0보다 큰 이름을 찾으면 된다.

## Java의 getOrDefault

Java에는 `Counter`에 해당하는 표준 도구가 없어 `HashMap`에 직접 누적해야 한다. 이때 없는 키를 조회하면 `null`이 반환되어 분기가 필요하다.

```java
if (map.containsKey(p)) {
    map.put(p, map.get(p) + 1);
} else {
    map.put(p, 1);
}
```

`getOrDefault()`를 사용하면 이 분기를 없앨 수 있다.

```java
map.put(p, map.getOrDefault(p, 0) + 1);
```

키가 존재하면 저장된 값을, 존재하지 않으면 0을 반환하므로 초기화 코드를 작성하지 않아도 된다.

## 최종 솔루션 코드

```python
from collections import Counter

def solution(participant, completion):
    # 1. 참가자 이름별 등장 횟수 집계
    count = Counter(participant)
    # 2. 완주자만큼 차감 → 완주하지 못한 1명만 값이 남음
    count.subtract(completion)
    # 3. 값이 0보다 큰 이름이 답
    for name, c in count.items():
        if c > 0:
            return name
```

```java
import java.util.HashMap;
import java.util.Map;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> map = new HashMap<>();
        // 1. 참가자 이름별 등장 횟수 누적
        for (String p : participant) {
            map.put(p, map.getOrDefault(p, 0) + 1);
        }
        // 2. 완주자만큼 차감
        for (String c : completion) {
            map.put(c, map.get(c) - 1);
        }
        // 3. 값이 0보다 큰 키가 답
        for (Map.Entry<String, Integer> e : map.entrySet()) {
            if (e.getValue() > 0) {
                return e.getKey();
            }
        }
        return "";
    }
}
```

## 성능 측정

로컬 측정 (n=100,000 무작위 케이스):

| 언어 | 예제 케이스 | n=100,000 | 메모리 |
|---|---|---|---|
| Python | 약 0.003 ms | 48.90 ms | 피크 5.50 MB |
| Java | 약 0.001~0.002 ms | 23.32 ms | 힙 증가 6.50 MB |

- 시간복잡도: **O(n)** — 두 명단을 각각 한 번씩 순회
- 공간복잡도: **O(n)** — 이름별 횟수를 저장하는 해시맵

## 요약

1. 리스트에서 값을 찾아 지우는 방식은 한 번에 O(n)이므로 n번 반복하면 O(n²)이 된다. n이 클 때는 사용할 수 없다.
2. 등장 횟수를 세야 할 때는 `값 → 횟수` 형태의 해시맵이 적합하다.
3. Python의 `Counter`와 `subtract`, Java의 `getOrDefault`를 알아두면 빈도 집계 코드를 간결하게 작성할 수 있다.

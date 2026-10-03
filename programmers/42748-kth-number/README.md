# [프로그래머스] K번째수 Python / Java

https://school.programmers.co.kr/learn/courses/30/lessons/42748
Lv.1 · 정렬

## 문제 분석 및 핵심 로직

commands의 각 원소 `[i, j, k]`에 대해, 배열의 i번째부터 j번째까지를 잘라 정렬한 뒤 k번째 수를 구하는 문제다.

**핵심 조건:**

1. **1-based 인덱스:** 문제의 i, j, k는 1부터 센다. Python/Java의 0-based 인덱스로 변환해야 한다.
2. **구간마다 독립적인 정렬:** 각 command의 구간이 다르므로, 전체를 한 번 정렬해 두고 재사용할 수 없다.
3. **규모:** array 길이 ≤ 100, commands 길이 ≤ 50으로 작다. 구간을 잘라 그때그때 정렬하는 단순한 방식이 충분하다.

## 1-based를 0-based로 바꾸는 방법

문제는 "2번째부터 5번째까지"라고 말하지만, 코드는 0부터 센다. 변환 규칙은 단순하다: 시작 인덱스는 1을 빼고, 끝 인덱스는 그대로 둔다.

```python
array = [1, 5, 2, 6, 3, 7, 4]
# i=2, j=5 → 2번째(5)부터 5번째(3)까지
array[1:5]   # [5, 2, 6, 3]
```

끝 인덱스를 그대로 두는 이유는 슬라이스의 끝이 exclusive이기 때문이다. `array[1:5]`는 인덱스 1, 2, 3, 4를 가져오는데, 이는 1-based로 2번째부터 5번째까지와 정확히 일치한다. Java의 `Arrays.copyOfRange(array, from, to)`도 같은 규칙이다. from은 1을 빼고, to는 그대로 둔다.

k번째 수도 마찬가지다. 정렬된 배열의 k번째는 인덱스 `k-1`이다.

## 복사본을 정렬해야 하는 이유

정렬은 원본 배열을 직접 건드리지 않아야 한다. 다음 command의 구간도 원본 array를 기준으로 자르기 때문이다.

Python의 `sorted()`는 새 리스트를 반환하므로 원본이 안전하다. 반면 리스트의 `.sort()` 메소드는 제자리에서 정렬하므로, 슬라이스(복사본)에 적용하면 원본에는 영향이 없다. 어느 쪽을 써도 원본은 보존된다.

```python
sliced = array[i-1:j]   # 슬라이스는 이미 복사본
sliced = sorted(sliced) # 새 리스트 반환, 원본 무관
```

Java에서는 `Arrays.copyOfRange()`로 구간을 복사한 뒤 `Arrays.sort()`로 정렬한다. `Arrays.sort(array, from, to)`처럼 원본에 직접 구간 정렬을 적용하는 방법도 있지만, 구간이 겹치는 command가 있을 경우 순서에 따라 결과가 달라질 수 있어 복사 후 정렬이 안전하다.

## 정렬을 직접 구현하지 않는 이유

초심자 방식은 정렬을 직접 구현하는 것이다. 예를 들어 버블 정렬로 구간을 정렬하면 구간 길이 L에 대해 O(L²)이 든다. commands가 m개면 전체 O(m·L²)이다.

내장 정렬을 사용하면 한 번의 정렬이 O(L log L)이다. Python의 `sorted()`는 Timsort, Java의 `Arrays.sort()`는 Dual-Pivot Quicksort를 사용한다. 둘 다 평균적으로 O(L log L)에 동작하며, 직접 구현한 O(L²) 정렬보다 구간이 길어질수록 차이가 벌어진다. 이 문제의 제한에서는 어느 쪽도 시간 초과가 나지 않지만, 정렬은 언어의 내장 도구에 맡기는 것이 정석이다.

## 최종 솔루션 코드

```python
def solution(array, commands):
    answer = []
    for i, j, k in commands:
        # 1. 1-based 구간 [i, j]를 0-based 슬라이스로 자르기 (끝은 exclusive라 j 그대로)
        sliced = array[i-1:j]
        # 2. 복사본 정렬 (원본 훼손 없음)
        sliced = sorted(sliced)
        # 3. k번째 수 (1-based → 0-based)
        answer.append(sliced[k-1])
    return answer
```

```java
import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int[] answer = new int[commands.length];
        for (int t = 0; t < commands.length; t++) {
            int i = commands[t][0];
            int j = commands[t][1];
            int k = commands[t][2];
            // 1. 1-based 구간 [i, j]를 0-based로 복사 (copyOfRange의 끝은 exclusive)
            int[] sliced = Arrays.copyOfRange(array, i - 1, j);
            // 2. 복사본 정렬 (원본 훼손 없음)
            Arrays.sort(sliced);
            // 3. k번째 수 (1-based → 0-based)
            answer[t] = sliced[k - 1];
        }
        return answer;
    }
}
```

## 성능 측정

로컬 측정 (n=100,000 무작위 배열, commands 50개 — 제한보다 크게 스케일업):

| 언어 | 예제 케이스 | n=100,000, commands 50 | 메모리 |
|---|---|---|---|
| Python | 0.0096 ms | 273.03 ms | 피크 1.63 MB |
| Java | 0.4029 ms | 109.11 ms | 힙 증가 0.26 MB |

- 시간복잡도: **O(m·L log L)** — command m개마다 길이 L인 구간을 잘라 정렬
- 공간복잡도: **O(L)** — 한 번에 하나의 구간 복사본만 유지

## 요약

1. 1-based 구간 [i, j]를 0-based로 바꿀 때는 시작만 1을 빼고 끝은 그대로 둔다. 슬라이스·copyOfRange의 끝이 exclusive이기 때문이다.
2. 정렬은 원본이 아닌 복사본에 적용해야 한다. 다음 command의 구간도 원본 기준이므로.
3. 정렬은 직접 구현하지 말고 내장 정렬에 맡긴다. O(L²)과 O(L log L)의 차이는 구간이 길어질수록 벌어진다.

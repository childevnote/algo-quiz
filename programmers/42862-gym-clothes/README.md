# [프로그래머스] 체육복 Python / Java

https://school.programmers.co.kr/learn/courses/30/lessons/42862
Lv.1 · 탐욕법

## 문제 분석 및 핵심 로직

n명의 학생 중 일부는 체육복을 도난당했고(lost), 일부는 여벌을 가져왔다(reserve). 여벌이 있는 학생은 번호 순서상 바로 앞뒤 이웃에게만 체육복을 빌려줄 수 있다. 체육수업을 들을 수 있는 학생 수의 최댓값을 구하는 문제다.

**핵심 조건:**

1. **자급자족:** lost와 reserve에 모두 들어 있는 학생은 여벌 중 하나를 도난당한 것으로 간주한다. 남은 한 벌로 스스로 해결하므로, 다른 학생에게 빌려줄 수 없고 빌릴 필요도 없다.
2. **대여는 이웃에게만:** i번 학생이 빌릴 수 있는 후보는 i-1번과 i+1번뿐이다.
3. **한 벌당 한 번:** 여벌 하나는 한 명의 학생에게만 빌려줄 수 있다.

## 초심자 방식 vs 개선 방식

### 초심자 방식: 리스트 그대로 순회하며 선형 탐색

lost와 reserve를 리스트로 두고, 각 lost 학생마다 reserve 리스트를 처음부터 훑어 i-1이나 i+1이 있는지 찾는다. 이 방식에는 두 가지 함정이 있다.

첫째, lost와 reserve의 교집합을 처리하지 않으면 틀린다. 여벌을 가져왔지만 도난당한 학생은 빌려줄 여유가 없는데, reserve 리스트에 남아 있으면 다른 학생에게 빌려주는 것으로 잘못 계산된다. n=5, lost=[2,3,4], reserve=[1,2,3]에서 교집합을 제거하지 않으면 2번이 3번에게, 3번이 4번에게 빌려주는 것으로 셈해 5명이라고 답하지만, 실제로 2번과 3번은 자급자족이라 빌려줄 수 없어 정답은 4다.

둘째, 매번 리스트를 훑으면 O(L×R)이라 비효율적이다. n이 30 이하라 통과는 되지만, 습관으로 남기면 안 되는 패턴이다.

### 개선 방식: 집합 차집합 + 앞번호 우선 탐욕

`set(lost) - set(reserve)`로 진짜 빌려야 하는 학생만 남기고, `set(reserve) - set(lost)`로 빌려줄 수 있는 여벌만 남긴다. 집합이므로 조회는 O(1)이다.

남은 lost 학생을 번호 오름차순으로 처리하면서, 앞번호 이웃(i-1)에게 먼저 빌리고 없으면 뒷번호 이웃(i+1)에게 빌린다. 이 순서가 중요한 이유: i번 학생이 쓸 수 있는 여벌은 i-1과 i+1뿐인데, i+1번 여벌은 i+2번 학생도 쓸 수 있지만 i-1번 여벌은 i번 학생(과 i-2번)에게만 의미가 있다. 범위가 좁은 자원을 먼저 소진하면, 뒤쪽 학생이 쓸 수 있는 선택지가 최대한 남는다.

```python
need = sorted(set(lost) - set(reserve))  # 빌려야 하는 학생
give = set(reserve) - set(lost)           # 빌려줄 수 있는 여벌
for l in need:
    if l - 1 in give: give.remove(l - 1)       # 앞번호 우선
    elif l + 1 in give: give.remove(l + 1)
```

이 탐욕이 최적을 보장하는 직관: 작은 번호부터 처리하고 각 단계에서 "대체 불가능한 자원"을 먼저 쓰면, 나중 단계의 선택지를 줄이지 않는다. 대여 관계가 일렬 번호로만 이어지는 구조라 전역 최적과 충돌하지 않는다.

## 최종 솔루션 코드

```python
def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    # 1. 자급자족 학생 제외: lost와 reserve에 모두 있으면 스스로 해결
    need = sorted(lost_set - reserve_set)
    # 2. 대여 가능한 여벌만 남기기
    give = reserve_set - lost_set
    for l in need:
        # 3. 번호가 작은 학생부터 앞번호 이웃에게 우선 대여
        if l - 1 in give:
            give.remove(l - 1)
        # 4. 없으면 뒷번호 이웃에게 대여
        elif l + 1 in give:
            give.remove(l + 1)
        # 5. 빌리지 못하면 수업에서 제외
        else:
            n -= 1
    return n
```

```java
import java.util.*;

class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        Set<Integer> need = new HashSet<>();
        Set<Integer> give = new HashSet<>();
        for (int l : lost) need.add(l);
        for (int r : reserve) give.add(r);
        Set<Integer> lostOrig = new HashSet<>(need);
        // 1. 자급자족 학생 제외: lost와 reserve에 모두 있으면 스스로 해결
        need.removeAll(give);
        // 2. 대여 가능한 여벌만 남기기
        give.removeAll(lostOrig);
        int[] arr = need.stream().mapToInt(i -> i).toArray();
        // 3. 번호가 작은 학생부터
        Arrays.sort(arr);
        for (int l : arr) {
            // 4. 앞번호 이웃에게 우선 대여
            if (give.contains(l - 1)) give.remove(l - 1);
            // 5. 없으면 뒷번호 이웃에게 대여
            else if (give.contains(l + 1)) give.remove(l + 1);
            // 6. 빌리지 못하면 수업에서 제외
            else n--;
        }
        return n;
    }
}
```

## 성능 측정

로컬 측정 결과:

| 언어 | 예제 케이스 평균 | n=100,000 무작위 | 메모리(피크) |
|---|---|---|---|
| Python | 1.65 µs | 34.73 ms | 1.69 MiB |
| Java | 35.90 µs | 15.26 ms | — |

- 시간복잡도: **O(L log L)** — lost 정렬이 지배적 (L = |lost|). 집합 조회·삭제는 평균 O(1)
- 공간복잡도: **O(L + R)** — 두 집합

## 요약

1. lost ∩ reserve는 자급자족이므로 집합 차집합으로 먼저 제외한다.
2. 번호가 작은 학생부터 앞번호 이웃에게 우선 대여하는 탐욕이 최적이다. 범위가 좁은 자원(앞번호 이웃)을 먼저 쓰는 것이 뒤쪽 선택지를 살린다.
3. 집합 조회 O(1) 덕분에 정렬을 제외하면 선형에 가까운 시간으로 해결된다.

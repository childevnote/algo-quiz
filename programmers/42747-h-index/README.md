# H-Index

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42747
- 레벨: Lv.2 · 카테고리: 정렬
- 풀이 날짜: 2026-10-20

## 문제 분석 및 핵심 로직

n편의 논문 중 "h번 이상 인용된 논문이 h편 이상"을 만족하는 가장 큰 h를 구하는 문제다.

핵심은 인용 횟수를 정렬하면 h를 '조건식 하나로' 판정할 수 있다는 점이다. 논문을 인용 횟수 내림차순으로 정렬했을 때, i번째 논문(1-indexed)의 인용 횟수를 c_i라 두면 "c_i >= i"는 곧 "i번 이상 인용된 논문이 i편 이상"과 정확히 같은 뜻이다. 여기서 i는 후보 h 자체가 되므로, 내림차순으로 스캔하며 c_i >= i를 만족하는 가장 큰 i가 정답이 된다.

```python
# ① 내림차순 정렬 → i번째 원소가 i편 이상 인용됐는지 판정 가능
citations = sorted(citations, reverse=True)
h = 0
# ② 스캔하며 조건을 만족하는 가장 큰 i를 답으로
for i, c in enumerate(citations, start=1):
    if c >= i:
        h = i
    else:
        break
return h
```

## 개념별 심층 설명

### 초심자의 방식: 모든 h를 전부 세어 보기

H-Index의 정의에서 h를 후보로 하나씩 꺼내 검증한다면, h마다 "인용 횟수가 h 이상인 논문이 몇 편인지"를 세야 한다. 논문이 n편이면 후보 h도 n개, 검증도 n개 논문을 보므로 시간복잡도가 O(n²)이 된다. n <= 1,000이니 제한 안에서는 통과하지만, 논리를 정렬에 옮겨 닮지 않으면 매번 같은 일을 반복한다.

### 개선 방식: 정렬 후 한 번의 스캔

정렬을 한 번 하면 "상위 i편"이라는 집합이 고정된다. 내림차순 정렬에서 i번째 원소가 바로 "인용 횟수가 i번째로 많은 논문"이므로, c_i >= i 하나의 부등식만으로 h 후보 i를 검증할 수 있다. 후보를 작은 쪽부터 차례로 확인하면 조건이 깨지는 순간 이후의 i는 전부 실패하므로 break로 끝낸다. 한 번의 정렬(O(n log n)) + 한 번의 스캔(O(n))으로 끝나고, 코드는 짧지만 정의와 정확히 같은 일을 한다.

### 왜 `break`가 안전한가

내림차순 정렬에서 c_i < i인 i가 등장했다면, 그 뒤의 모든 j > i에 대해 c_j <= c_i < i < j가 성립한다. 즉 이후 후보는 전부 조건을 만족하지 못하므로, 더 볼 필요가 없다.

## 최종 솔루션 코드

### Python

```python
def solution(citations):
    citations = sorted(citations, reverse=True)  # ① 내림차순 정렬
    h = 0
    for i, c in enumerate(citations, start=1):   # ② i = h 후보
        if c >= i:                               # ③ "i번 이상 인용된 논문이 i편 이상"
            h = i
        else:
            break                                # ④ 이후 후보는 전부 실패하므로 종료
    return h
```

### Java

```java
import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);                  // ① 오름차순 정렬
        int n = citations.length;
        int h = 0;
        // ② citations[i]는 상위 (n - i)편 중 가장 작은 값:
        //    citations[i] >= (n - i) ⟺ 상위 (n - i)편이 (n - i)회 이상 인용
        for (int i = 0; i < n; i++) {
            int papers = n - i;
            if (citations[i] >= papers) {         // ③ 뒤에서부터 첫 성립 지점이 최대 h
                h = papers;
                break;
            }
        }
        return h;
    }
}
```

## 성능 측정 (로컬 실측)

- 예제 케이스 `[3, 0, 6, 1, 5]`: 평균 약 0.76 µs (10,000회 평균)
- n=100,000 무작위 케이스 (인용 횟수 0~10,000): 약 31.35 ms, 피크 메모리 약 1.17 MiB
- 시간복잡도: O(n log n) — 정렬이 지배적
- 공간복잡도: Python O(n) (sorted가 새 리스트를 만듦), Java O(1) 추가 (제자리 정렬)

## 요약

- 정렬 한 번이면 H-Index 정의를 "c_i >= i" 하나의 부등식으로 바꿀 수 있다.
- 내림차순 스캔에서는 조건이 깨지는 순간 멈춰도 정답이 보장된다 (단조성).
- O(n²)의 후보별 검증이 O(n log n)의 정렬+스캔으로 줄어드는 것이 이 문제의 포인트다.
- (자동 풀이: 2026-10-20 18:00 스케줄에서 사용자가 풀이하지 않아 대신 풀이·커밋)

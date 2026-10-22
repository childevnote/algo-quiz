# 소수 찾기

- 문제 링크: https://school.programmers.co.kr/learn/courses/30/lessons/42839
- 레벨: Lv.2 · 카테고리: 완전탐색
- 풀이 날짜: 2026-10-21

## 문제 분석 및 핵심 로직

흩어진 숫자 종이 조각(numbers, 길이 1~7)으로 만들 수 있는 서로 다른 소수가 몇 개인지 세는 문제다. 길이는 7 이하이므로 모든 길이(1~7)의 순열을 전부 만들어 보면 되는데, 그 개수는 최대 P(7,1)+…+P(7,7) = 13,699개로 작다. 완전탐색이 정당한 경우다.

핵심은 두 가지다. 첫째, 순열에서 만든 문자열을 숫자로 바꿀 때 `int()` 변환으로 앞자리 0을 소거한다 — "011" → 11, "0" → 0. 둘째, 중복되는 숫자는 set에 모아 한 번만 센다 — 같은 숫자가 여러 순열에서 나와도 소수 판정은 한 번만 하면 된다.

소수 판정은 √n까지 나눠 보는 것으로 충분하다. 후보 중 가장 큰 수는 7자리(9,999,999 이하)라 √n ≈ 3,162까지만 검사하면 되고, 짝수는 n == 2 제외하고 바로 탈락시킨다.

```python
# ① 모든 길이의 순열로 후보 숫자 생성 (set으로 중복 제거)
candidates = set()
for length in range(1, len(numbers) + 1):
    for p in permutations(numbers, length):
        candidates.add(int("".join(p)))   # 앞자리 0은 int 변환으로 소거
# ② 소수만 카운트
return sum(1 for n in candidates if is_prime(n))
```

## 개념별 심층 설명

### 초심자의 방식: 모든 조합을 일일이 소수 판정하되 중복을 무시하기

순열을 돌면서 매번 소수 판정을 하면, "011" 같은 입력에서 11이 여러 번 만들어질 때마다 같은 판정을 반복한다. 더 흔한 실수는 "0으로 시작하는 숫자"를 따로 처리하려다 코드가 꼬이는 것이다. 순열 자체를 만들 때와 숫자로 바꾸는 순간을 분리해서 생각하면 두 문제 다 해결된다.

### 개선 방식: 숫자 변환 + set으로 후보 정리, 그 다음 판정

순열에서 문자열을 숫자로 바꾸는 단계(`int("".join(p))`)에서 앞자리 0 문제가 사라진다 — 문자열 처리로 골머리 썩을 일이 없다. 그리고 모든 후보를 set에 먼저 모아두면 중복 판정이 원천 제거된다. 판정 단계에서는 √n까지만 나누는 기본 검사가 후보 수(≤13,699)에 대해 충분히 빠르다. 다만 Python 실측에서 최악 입력이 1.15초로 간당간당하므로, 더 빠른 실행이 필요하면 9,999,999까지 에라토스테네스의 체를 한 번 깔아 판정을 O(1)로 바꾸는 선택지가 있다.

### 왜 Java는 수십 배 빠른가

같은 알고리즘이라도 Python의 `itertools.permutations`는 13,699개의 튜플을 만들어 문자열 join까지 해야 하는 반면, Java는 DFS로 숫자를 직접 누적(`current * 10 + digit`)한다. 튜플·문자열 같은 중간 객체가 없어 최악 입력이 6.79ms로 끝난다. 알고리즘이 같아도 언어별 비용 구조가 다르다는 점을 체감할 수 있는 문제다.

## 최종 솔루션 코드

### Python

```python
from itertools import permutations

def solution(numbers):
    candidates = set()                                   # ① 중복 숫자 제거용
    for length in range(1, len(numbers) + 1):            # ② 길이 1부터 전부
        for p in permutations(numbers, length):
            candidates.add(int("".join(p)))             # ③ 앞 0 소거 + set 삽입
    return sum(1 for n in candidates if is_prime(n))    # ④ 소수만 셈

def is_prime(n):
    if n < 2:                                           # ⑤ 0, 1은 소수 아님
        return False
    if n == 2:                                          # ⑥ 2는 유일한 짝수 소수
        return True
    if n % 2 == 0:                                      # ⑦ 짝수는 바로 탈락
        return False
    i = 3                                               # ⑧ 홀수 약수만 √n까지 검사
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```

### Java

```java
import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(String numbers) {
        Set<Integer> candidates = new HashSet<>();        // ① 중복 숫자 제거용
        dfs(numbers, new boolean[numbers.length()], 0, 0, candidates); // ② DFS 순열
        int answer = 0;
        for (int n : candidates)                          // ③ 소수만 셈
            if (isPrime(n)) answer++;
        return answer;
    }

    // ④ 자릿수에 숫자를 누적하며 DFS — "011"도 11이 된다 (앞 0 자동 소거)
    private void dfs(String numbers, boolean[] used, int current, int depth, Set<Integer> candidates) {
        if (depth > 0) candidates.add(current);
        for (int i = 0; i < numbers.length(); i++) {
            if (!used[i]) {
                used[i] = true;
                dfs(numbers, used, current * 10 + (numbers.charAt(i) - '0'), depth + 1, candidates);
                used[i] = false;                          // ⑤ 백트래킹
            }
        }
    }

    private boolean isPrime(int n) {                      // ⑥ √n까지 약수 판정
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0) return false;
        return true;
    }
}
```

## 성능 측정 (로컬 실측)

- 예제 케이스 `"17"`: Python 평균 약 0.0030 ms / Java 평균 약 0.0012 ms (10,000회 평균)
- 예제 케이스 `"011"`: Python 평균 약 0.0063 ms / Java 평균 약 0.0035 ms (10,000회 평균)
- 최악 입력 `"7654321"` (순열 13,699개, 소수 1,336개): Python 약 1,145 ms, 피크 메모리 약 0.86 MiB / Java 약 6.79 ms
- 시간복잡도: O(P(n) × √M) — P(n)은 순열 수(최대 13,699), M은 최대 후보값(10⁷ 미만)
- 공간복잡도: O(P(n)) — 후보 set 저장

## 요약

- 길이가 7 이하라 순열이 13,699개 이하 — 완전탐색이 정당한 문제다.
- `int()` 변환으로 앞자리 0을 소거하고, set으로 중복 판정을 없앤다.
- 소수 판정은 √n까지 나눗셈으로 충분하다.
- 같은 알고리즘도 언어별 비용 구조가 다르다 (최악 입력 Python 1,145 ms vs Java 6.79 ms).
- (자동 풀이: 2026-10-21 18:00 스케줄에서 사용자가 풀이하지 않아 대신 풀이·커밋)

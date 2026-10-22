# 개념 정리 — 소수 찾기

## 순열 (Permutation)

서로 다른 n개 중 r개를 뽑아 순서대로 나열하는 경우의 수를 P(n, r) = n! / (n-r)! 이라 한다. r = 1부터 n까지 전부 합하면 n이 작을 때(예: n = 7 → 13,699) 전수 탐색이 실용적이다.

```python
from itertools import permutations

list(permutations("abc", 2))
# [('a','b'), ('a','c'), ('b','a'), ('b','c'), ('c','a'), ('c','b')]
```

Java에는 표준 라이브러리에 순열 함수가 없어 DFS + `used` 배열로 직접 구현하는 것이 정석이다: `used[i]`가 이미 쓴 원소를 표시하고, 재귀 진입 전 true·복귀 후 false로 되돌리는 백트래킹 패턴.

```java
void perm(int[] arr, boolean[] used, int depth) {
    if (depth == arr.length) { /* 하나의 순열 완성 */ return; }
    for (int i = 0; i < arr.length; i++) {
        if (!used[i]) {
            used[i] = true;
            perm(arr, used, depth + 1);
            used[i] = false;   // 백트래킹: 다음 분기를 위해 되돌림
        }
    }
}
```

## 소수 판정 — √n까지 나누기

n이 합성수라면 n = a × b인 약수 쌍 중 하나는 반드시 √n 이하다. 따라서 2부터 √n까지 나누어 떨어지는 수가 하나라도 있으면 합성수, 없으면 소수다. 짝수는 2를 제외하고 전부 합성수이므로, 2를 먼저 처리하고 홀수 약수만 검사하면 절반으로 줄어든다.

```python
def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0: return False
        i += 2
    return True
```

## 에라토스테네스의 체 (Sieve of Eratosthenes)

많은 수에 대해 소수 여부를 반복 판정해야 할 때는 체가 유리하다. 2부터 시작해 소수의 배수를 차례로 지우면 남은 수가 모두 소수다. N까지 체를 만드는 비용은 O(N log log N), 이후 판정은 O(1)이다.

```python
def sieve(n):
    is_p = [True] * (n + 1)
    is_p[0] = is_p[1] = False
    i = 2
    while i * i <= n:
        if is_p[i]:
            for j in range(i * i, n + 1, i):
                is_p[j] = False
        i += 1
    return is_p

is_p = sieve(100)
# is_p[97] -> True, is_p[100] -> False
```

판정 횟수가 적으면 √n 나누기가 간단하고, 후보가 수만 개 이상으로 많아지면 체 한 번이 전체 시간을 줄인다. 이 문제처럼 최대 후보값이 9,999,999 이하인 경우 체 크기도 1,000만 bool 정도로 고정되므로 선택지가 된다.

## 문자열 숫자와 앞자리 0

문자열로 만든 숫자("007")는 정수로 바꾸는 순간 앞자리 0이 소거된다: `int("007")` → 7. 반대로 숫자를 문자열로 이어 붙일 때는 `str()` 변환이 필요하다.

```python
int("007")          # 7
"".join(["0", "0", "7"])  # "007"
```

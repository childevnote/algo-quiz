# https://school.programmers.co.kr/learn/courses/30/lessons/12928
# 2026-11-23

def solution(n):
    # 1. 약수는 짝을 이룬다: i가 n의 약수이면 n // i도 n의 약수이다.
    # 2. 1부터 sqrt(n)까지만 확인하면 모든 약수 쌍을 찾을 수 있다.
    #    i * i == n인 경우(제곱수)는 i를 한 번만 더한다.
    # 3. n이 0이면 약수가 없으므로 0을 반환한다.
    if n == 0:
        return 0
    total = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            total += i
            if i * i != n:
                total += n // i
        i += 1
    return total

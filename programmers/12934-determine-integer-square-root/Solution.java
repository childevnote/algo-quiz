class Solution {
    public long solution(long n) {
        // 1. 부동소수점으로 근사 제곱근을 구한다.
        // 2. 근사값이 실제 제곱근보다 크거나 작을 수 있으므로 ±1 범위로 보정한다.
        // 3. 보정된 x의 제곱이 n과 같으면 (x+1)의 제곱을, 다르면 -1을 반환한다.
        // n은 최대 50,000,000,000,000이므로 long으로 받는다.
        long x = (long) Math.sqrt(n);
        while ((x + 1) * (x + 1) <= n) x++;
        while (x * x > n) x--;
        if (x * x == n) {
            return (x + 1) * (x + 1);
        }
        return -1;
    }
}

class Solution {
    public int solution(int n) {
        // 1. 약수는 짝을 이룬다: i가 n의 약수이면 n / i도 n의 약수이다.
        // 2. 1부터 sqrt(n)까지만 확인하면 모든 약수 쌍을 찾을 수 있다.
        //    i * i == n인 경우(제곱수)는 i를 한 번만 더한다.
        // 3. n이 0이면 약수가 없으므로 0을 반환한다.
        if (n == 0) {
            return 0;
        }
        int total = 0;
        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                total += i;
                if (i * i != n) {
                    total += n / i;
                }
            }
        }
        return total;
    }
}

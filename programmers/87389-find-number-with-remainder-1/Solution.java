class Solution {
    public int solution(int n) {
        // 1. n % x == 1 이면 n - 1은 x의 배수이다. (단, 나머지가 1이려면 x > 1)
        // 2. 따라서 답은 n - 1의 1보다 큰 가장 작은 약수이다.
        // 3. 약수는 sqrt(n - 1)까지만 검사하면 된다. 약수가 없으면 n - 1 자체가 소수이므로 답은 n - 1이다.
        int m = n - 1;
        for (int x = 2; (long) x * x <= m; x++) {
            if (m % x == 0) {
                return x;
            }
        }
        return m;
    }
}

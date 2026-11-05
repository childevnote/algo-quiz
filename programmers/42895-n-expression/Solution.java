import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

class Solution {
    public int solution(int N, int number) {
        // 1. dp[i]: N을 i번 사용해서 만들 수 있는 수들의 집합 (long: 중간 곱셈 오버플로 방지)
        List<Set<Long>> dp = new ArrayList<>();
        for (int i = 0; i < 9; i++) {
            dp.add(new HashSet<>());
        }
        for (int i = 1; i <= 8; i++) {
            // 2. N을 i번 이어붙인 수 (예: N=5, i=3 -> 555)
            long concat = 0;
            for (int k = 0; k < i; k++) {
                concat = concat * 10 + N;
            }
            dp.get(i).add(concat);
            // 3. i번을 j번과 i-j번으로 나눠 사칙연산으로 조합
            for (int j = 1; j < i; j++) {
                for (long a : dp.get(j)) {
                    for (long b : dp.get(i - j)) {
                        dp.get(i).add(a + b);
                        dp.get(i).add(a - b);
                        dp.get(i).add(a * b);
                        if (b != 0) {
                            dp.get(i).add(Math.floorDiv(a, b));
                        }
                    }
                }
            }
            // 4. number를 처음 만든 횟수가 최솟값
            if (dp.get(i).contains((long) number)) {
                return i;
            }
        }
        return -1;
    }
}

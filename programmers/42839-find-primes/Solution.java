import java.util.HashSet;
import java.util.Set;

class Solution {
    public int solution(String numbers) {
        // [1] DFS로 모든 길이의 순열을 만들어 후보 숫자를 만든다
        Set<Integer> candidates = new HashSet<>();
        boolean[] used = new boolean[numbers.length()];
        dfs(numbers, used, 0, 0, candidates);

        // [2] 소수만 셈한다
        int answer = 0;
        for (int n : candidates) {
            if (isPrime(n)) answer++;
        }
        return answer;
    }

    // 자릿수에 숫자를 붙이며 DFS: current * 10 + digit 으로 "011" -> 11 처럼 앞 0 자동 소거
    private void dfs(String numbers, boolean[] used, int current, int depth, Set<Integer> candidates) {
        if (depth > 0) {
            candidates.add(current);
        }
        for (int i = 0; i < numbers.length(); i++) {
            if (!used[i]) {
                used[i] = true;
                dfs(numbers, used, current * 10 + (numbers.charAt(i) - '0'), depth + 1, candidates);
                used[i] = false;
            }
        }
    }

    // [3] 에라토스테네스식 약수 판정: sqrt(n)까지만 나눈다
    private boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }
}

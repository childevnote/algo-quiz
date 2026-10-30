class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(numbers, target, 0, 0);
    }

    // 1. 재귀 DFS: 각 숫자를 더하거나 빼는 두 갈래로 탐색
    private int dfs(int[] numbers, int target, int idx, int total) {
        // 2. 모든 숫자를 사용했으면 합이 target인지 확인
        if (idx == numbers.length) {
            return total == target ? 1 : 0;
        }
        // 3. 현재 숫자를 더하는 경우와 빼는 경우를 합산
        return dfs(numbers, target, idx + 1, total + numbers[idx])
             + dfs(numbers, target, idx + 1, total - numbers[idx]);
    }
}

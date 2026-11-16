class Solution {
    public int solution(String[] arr) {
        int n = (arr.length + 1) / 2;
        int[] nums = new int[n];
        char[] ops = new char[n - 1];
        for (int i = 0; i < n; i++) nums[i] = Integer.parseInt(arr[2 * i]);
        for (int i = 0; i < n - 1; i++) ops[i] = arr[2 * i + 1].charAt(0);

        int[][] mx = new int[n][n];
        int[][] mn = new int[n][n];
        for (int i = 0; i < n; i++) {
            mx[i][i] = mn[i][i] = nums[i];
        }
        for (int len = 2; len <= n; len++) {
            for (int i = 0; i + len - 1 < n; i++) {
                int j = i + len - 1;
                mx[i][j] = Integer.MIN_VALUE;
                mn[i][j] = Integer.MAX_VALUE;
                for (int k = i; k < j; k++) {
                    if (ops[k] == '+') {
                        mx[i][j] = Math.max(mx[i][j], mx[i][k] + mx[k + 1][j]);
                        mn[i][j] = Math.min(mn[i][j], mn[i][k] + mn[k + 1][j]);
                    } else {
                        mx[i][j] = Math.max(mx[i][j], mx[i][k] - mn[k + 1][j]);
                        mn[i][j] = Math.min(mn[i][j], mn[i][k] - mx[k + 1][j]);
                    }
                }
            }
        }
        return mx[0][n - 1];
    }
}

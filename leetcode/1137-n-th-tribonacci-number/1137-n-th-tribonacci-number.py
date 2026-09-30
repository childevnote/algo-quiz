class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0, 1, 1]; [arr.append(arr[-1] + arr[-2] + arr[-3]) for _ in range(36)]

        return arr[n]
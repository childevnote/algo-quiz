class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,2,3]
        for i in range(3, 45):
            arr.append(arr[i - 1] + arr[i - 2])
        return arr[n-1]

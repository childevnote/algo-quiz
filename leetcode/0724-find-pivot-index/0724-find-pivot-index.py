class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rightsum=sum(nums)
        leftsum=0
        for i, num in enumerate(nums):
            rightsum -= num
            if leftsum == rightsum:
                return i
            leftsum += num
        return -1


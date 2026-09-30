class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        streak = 0
        result = 0
        
        for z in nums:
            if z == 0:
                streak += 1
            else:
                if streak > 0:
                    result += streak * (streak + 1) // 2
                    streak = 0

        result += streak * (streak + 1) // 2

        return result
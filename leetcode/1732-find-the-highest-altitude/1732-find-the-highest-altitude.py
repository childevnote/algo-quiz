class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result= [0]
        init = 0
        for i in gain:
            init += i
            result.append(init)

        return max(result)
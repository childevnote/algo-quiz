class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        for i in reversed(s.split()):
            res.append(i)
        return ' '.join(res)
        
        
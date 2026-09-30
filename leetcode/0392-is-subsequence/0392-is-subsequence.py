class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        if len(s) == 0:
            return True
        index = 0
        for w in t:
            if index < len(s) and w == s[index] :
                index += 1
        
        return True if len(s)==index else False
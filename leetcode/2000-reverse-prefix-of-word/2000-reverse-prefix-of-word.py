class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        if n==-1:
            return word
        else :
            return word[n::-1]+word[n+1:]
        
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        vowels_inS = [v for v in s if v in vowels]
        answer = [vowels_inS.pop() if char in vowels else char for char in s]

        return "".join(answer)
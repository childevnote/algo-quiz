class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiou"
        v_num = sum(s[i] in vowels for i in range(k))
        v_max = v_num
        for i in range(k, len(s)):
            if s[i - k] in vowels:
                v_num -= 1
            if s[i] in vowels:
                v_num += 1
            v_max = max(v_max, v_num)
        return v_max

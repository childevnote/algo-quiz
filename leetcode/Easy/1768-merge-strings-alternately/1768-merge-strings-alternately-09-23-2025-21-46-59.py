class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        index = 0
        while len(word1)+len(word2):
            if len(word1) == 0:
                output = output + word2
                break
            elif len(word2) == 0 :
                output = output + word1
                break
            if index %2 == 0:
                output = output + word1[0]
                word1 = word1[1:]
            else :
                output = output + word2[0]
                word2 = word2[1:]
            index += 1


        return output
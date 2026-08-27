class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        final = ""
        index = 0
        for i , n in enumerate(word1):
            if len(word2) != index:
                final += n
                final += word2[index]
                index += 1
            else:
                final += n      
        if len(word1) < len(word2):
            final += word2[index]
            index += 1
            while index != len(word2):
                final += word2[index]
                index += 1
        return final

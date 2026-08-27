class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_1 = list()
        anagram_2 = list()
        for i in s:
            anagram_1.append(i)
        for i in t:
            anagram_2.append(i)
        anagram_1.sort()
        anagram_2.sort()
        if anagram_2 == anagram_1:
            return(True)
        return(False)
        
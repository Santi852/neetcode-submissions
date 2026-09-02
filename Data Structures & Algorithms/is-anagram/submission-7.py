class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        anagram_1 = set()
        anagram_2 = set()
        for i in s:
            anagram_1.add(i)
        for i in t:
            anagram_2.add(i)
        if anagram_2 == anagram_1:
            return(True)
        return(False)
        
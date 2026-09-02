class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmapp = {}
        for i in s:
            hashmap.add(i)
        for n in t:
            hashmapp.add(n)
        if hashmapp == hashmap:
            return True
        else:
            return False
            
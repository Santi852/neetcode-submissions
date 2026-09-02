class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = set()
        hashmapp = set()
        for i in s:
            hashmap.add(i)
        for n in t:
            hashmapp.add(n)
        if hashmapp == hashmap:
            return True
        else:
            return False
            
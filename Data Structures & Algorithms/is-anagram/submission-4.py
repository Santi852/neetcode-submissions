class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashmap = {}
        hashmapp = {}
        for i in s:
            hashmap[i] = hashmap.get(i, 0) 
        for n in t:
            hashmapp[n] = hashmapp.get(n, 0) 
        if hashmapp == hashmap:
            return True
        else:
            return False

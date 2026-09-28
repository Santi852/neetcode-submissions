class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        res = int(h / piles[-1])
        if res == 0:
            return (piles[-1])
        return res
        
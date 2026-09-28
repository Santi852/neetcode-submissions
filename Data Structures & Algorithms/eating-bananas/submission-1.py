class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        while l <= r:
            count = 0
            middle = (l + r) // 2
            for i, n in enumerate(piles):
                count += math.ceil(n / middle)
            if count <= h:
                r = middle - 1
                res = middle
            else:
                l = middle + 1
        return res

                


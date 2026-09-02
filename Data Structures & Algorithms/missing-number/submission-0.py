class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if nums[0] != 0:
            return 0
        for i, n in enumerate(nums):
            if n + 1 == nums[i+1]:
                continue
            else:
                return n + 1
            


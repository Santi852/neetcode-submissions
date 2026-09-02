class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i, n in enumerate(nums):
            if n == len(nums):
                continue
            elif n + 1 == nums[i+1]:
                continue
            else:
                return n + 1
            


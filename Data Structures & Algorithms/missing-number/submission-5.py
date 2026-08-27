class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                return n + 1
            elif n + 1 == nums[i+1]:
                continue
            else:
                return n + 1
            


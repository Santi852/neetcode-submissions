class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for index, num in enumerate(nums):
            if index == len(nums) - 1:
                continue
            elif nums[index] == nums[index + 1]:
                return True
        return False
            



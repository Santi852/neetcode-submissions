class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        for index, num in enumerate(nums):
            if target - nums[index] in nums:
                return [index,nums.index(target - nums[index])]
        return [0,0]
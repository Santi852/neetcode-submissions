class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        for index, num in enumerate(nums):
            if index == len(nums) - 1:
                continue
            elif nums[index] + nums[index + 1] == target:
                return [index, index + 1]
        return [0,2]
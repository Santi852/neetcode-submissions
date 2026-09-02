class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            complement = target - nums[index]
            if complement in nums:
                complement_index = nums.index(complement, index + 1)
                if complement_index != -1:
                    return [index, complement_index]
        return [0,0]
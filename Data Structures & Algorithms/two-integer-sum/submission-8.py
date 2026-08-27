class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            s = nums[i]
            for j in range(i + 1, len(nums)):
                if s + nums[j] == target:
                    return [i, j]
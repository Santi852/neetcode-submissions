class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for s in range(len(nums)):
                if i != s and nums[i] + nums[s] == target:
                    return [i,s]
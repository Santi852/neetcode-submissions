class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 0
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                count += 1
            elif n == nums[i+1]:
                nums.remove(n)
            else:
                count += 1
        return count

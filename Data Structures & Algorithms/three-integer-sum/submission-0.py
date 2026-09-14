class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output = []
        a = 0
        while a < len(nums) - 2:
            if nums[a] > 0:
                break
            if a > 0 and nums[a] == nums[a - 1]:
                a += 1
            left = a + 1
            right = len(nums) - 1
            while left < right:
                total = nums[left] + nums[right] + nums[a]
                if total < 0:
                    left += 1
                elif total > 0:
                    right += -1
                else:
                    output.append([nums[a], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
            a += 1
        return output
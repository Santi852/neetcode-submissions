class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        direction = 0
        if len(nums) == 1:
            return True
        for i in range(len(nums) - 1):
            if direction == 0:
                if nums[i] > nums[i+1]:
                    direction = -1
                elif nums[i] < nums[i+1]:
                    direction = 1
            else:
                if nums[i+1] > nums[i] and direction == -1:
                    return False
                elif nums[i+1] < nums[i] and direction == 1:
                    return False
        return True

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        lp = 0
        Rp = len(heights) - 1
        max_area = 0
        
        while lp < Rp:
            # Calculate area between current pointers
            width = Rp - lp
            current_height = min(heights[lp], heights[Rp])
            area = width * current_height
            max_area = max(max_area, area)
            
            # Move the pointer with smaller height
            if heights[lp] < heights[Rp]:
                lp += 1
            else:
                Rp -= 1
        
        return max_area


        
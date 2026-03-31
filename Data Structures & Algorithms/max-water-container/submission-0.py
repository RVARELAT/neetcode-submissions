class Solution:
    def maxArea(self, heights: List[int]) -> int:  
        left = 0
        right = len(heights) - 1
        
        max_area = 0
        
        while left < right:
            # use the smallest height
            
            # left is the smaller height
            if heights[left] <= heights[right]:
                #  heck if new max area is greater
                if (heights[left] * (right - left)) > max_area:
                    max_area = heights[left] * (right - left)
                left += 1
            # right is the smaller height
            else:
                if (heights[right] * (right - left)) > max_area:
                    max_area = (heights[right] * (right - left))
                right -= 1
        
        return max_area

        
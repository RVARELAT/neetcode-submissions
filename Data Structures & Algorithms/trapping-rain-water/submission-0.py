class Solution:
    def trap(self, height: List[int]) -> int:
        # no heights given
        if height == []:
            return 0
        
        # two pointers
        left = 0 
        right = len(height) - 1
        
        max_left = height[left]
        max_right = height[right]
        max_area = 0
        
        while left < right:
            # left height is higher
            if height[left] <= height[right]:
                # only add to max_area if area were trying to add is > 0
                if max_left - height[left] > 0:
                    max_area += max_left - height[left]
                # only update max left if we find something higher
                if height[left] > max_left:
                    max_left = height[left]
                left += 1
            else:
                if max_right - height[right] > 0:
                    max_area += max_right - height[right]
                if height[right] > max_right:
                    max_right = height[right]
                right -= 1
            
        return max_area
            
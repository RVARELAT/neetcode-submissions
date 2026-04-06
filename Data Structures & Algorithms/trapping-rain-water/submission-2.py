class Solution:
    def trap(self, height: List[int]) -> int:
                
        if len(height) == []:
            return 0
        
        left = 0
        right = len(height) - 1
        
        left_max = height[left]
        right_max = height[right]
        
        result = 0
        
        while left < right:
            # shift left pointer
            if left_max < right_max:
                left += 1
                # compare left)max with curr height
                left_max = max(left_max, height[left])
                # left max is our bottleneck in this case
                result += left_max - height[left] # technically will never be negative (so left_max will be at most 0 given above check)

            # shift right pounter
            else:
                right -= 1
                right_max = max(right_max, height[right])
                result += right_max - height[right]
        
        return result
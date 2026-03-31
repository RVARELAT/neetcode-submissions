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
            # Use the *current heights* to decide which pointer to move
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

# 🕒 Time Complexity: O(n)
# You only go through the list once using two pointers (left and right).
# Each step moves one of them inward, and no element is visited more than once.
# ✅ So total work grows linearly with the number of bars.
# Example:
# If the input has 10 bars, you do about 10 steps.
# If it has 1000 bars, you do about 1000 steps.

# 💾 Space Complexity: O(1)
# You only keep a few variables: left, right, max_left, max_right, and max_area.
# No extra arrays or data structures are created.
# ✅ So it uses constant extra memory, no matter how big the input is.
            
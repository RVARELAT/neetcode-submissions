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

# ⏱ Time Complexity: O(n)
# You start with two pointers: one at the left end, one at the right end.
# In each step, you move one pointer closer toward the other — never both at once.
# So each index is visited at most once by either pointer.
# That means the total number of steps is about n, where n = number of heights.
# ✅ Result: O(n)

# 💾 Space Complexity: O(1)
# You only store a few variables: left, right, and max_area.
# You don’t create any extra lists or data structures that grow with the input size.
# ✅ Result: O(1)
        
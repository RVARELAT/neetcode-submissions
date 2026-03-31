class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # assume all elements are unique
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # found target
            if nums[mid] == target:
                return mid 
            
            # check if left side is sorted
            if nums[left] <= nums[mid]:
                # target not within left sorted part
                if target > nums[mid] or target < nums[left]:
                    # search the right side
                    left = mid + 1
                # target is within left sorted portion
                else:
                    right = mid -  1
            
            # check if right side is sorted
            if nums[mid] <= nums[right]:
                # target not within right sorted part
                if target < nums[mid] or target > nums[right]:
                    # search the left side
                    right = mid - 1
                # target is within right sorted portion
                else:
                    left = mid + 1
            
        # target not present
        return -1

# ✅ Time Complexity — O(log n)
# Why?
# This is a modified binary search.
# Each loop cuts the search space in half — either the left half or the right half.
# When you keep halving a list of size n, the number of steps is about log₂(n).
# In simple words:
# You never scan the whole array. You keep jumping to the middle and eliminating half of the array each time. That’s why it’s extremely fast.

# ✅ Space Complexity — O(1)
# Why?
# You only use a few variables: left, right, mid.
# No extra lists, no recursion, no additional data structures.
# The memory used does not grow with input size.
# In simple words:
# You use the same small amount of memory no matter how big the array is. Just three pointers, nothing more.
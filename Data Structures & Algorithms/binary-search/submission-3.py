class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # we dont want the the length from the left to the right pointer
            # we want to know the midpoint between them
            mid = (left + right) // 2
            # deals with integer overflow 
            # mid = left + (right - left) // 2
            # found target
            if target == nums[mid]:
                return mid 
            # target is on left side
            elif target < nums[mid]:
                right = mid - 1
            # target is on right side
            else:
                left = mid + 1
        # target not found
        return -1
        
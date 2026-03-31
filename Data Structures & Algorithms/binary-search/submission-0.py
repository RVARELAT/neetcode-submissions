class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            # use mid pointet to find target (take avergae of left and right pointers)
            mid = (right + left) // 2
            # found target
            if nums[mid] == target:
                return mid
            # check if mid number is greater than our target, if so, move right pointer before mid
            elif nums[mid] > target:
                right = mid - 1
            # else we assume mid number is less than our target
            # nums[mid] < target
            else:
                left = mid + 1
                
        # index does not exist
        return -1

# Time complexity: O(logn)
# Space Complexity: O(1)
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
                # lets search the left side
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                # else we automatically search the right side
                else:
                    left = mid + 1
            
            # check if right side is sorted
            if nums[mid] <= nums[right]:
                # lets search the right side
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    # search the left side
                    right = mid - 1
            
                
        # target not present
        return -1
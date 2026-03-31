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
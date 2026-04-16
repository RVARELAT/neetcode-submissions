class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            # nums[mid] < nums[right]
            else: 
                right = mid
                
        min_index = left
        
        # perform normal binary search      
        if min_index == 0:
            left = 0 
            right = len(nums) - 1
            
        # binary search on left side
        elif target >= nums[0] and target <= nums[min_index - 1]:
            left = 0
            right = min_index - 1
        
        # binary serach on right side
        else:
            left = min_index
            right = len(nums) - 1
            
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            
            # search right side
            elif target > nums[mid]:
                left = mid + 1
            # search left side
            else:
                right = mid - 1
                
        # target not found
        return -1

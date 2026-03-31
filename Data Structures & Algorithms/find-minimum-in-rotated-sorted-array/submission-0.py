class Solution:
    def findMin(self, nums: List[int]) -> int:
        # initialize left and right pointers
        left = 0
        right = len(nums) - 1
        # variable to track current minimum
        curr_min = float('inf')
        
        while left <= right:
            # if part were looking at is sorted already  
            if nums[left] <= nums[right]:
                if nums[left] < curr_min:
                    curr_min = nums[left]
                    # break out of while loop as we found min
                    break

            # // is integer division
            mid = (left + right) // 2
            
            # update current minimum using nums[mid]
            if nums[mid] < curr_min:
                curr_min = nums[mid]
            
            # min has to be on right side (since mid is a part of the left sorted portion)
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                # min has to be on the left side (since mid is a part of the right sorted portion)
                right = mid - 1
        
        return curr_min
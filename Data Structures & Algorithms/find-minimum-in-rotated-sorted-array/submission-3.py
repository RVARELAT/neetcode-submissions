class Solution:
    def findMin(self, nums: List[int]) -> int:       
        left = 0 
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            # pivot is on right side
            if nums[mid] > nums[right]:
                left = mid + 1
            # mid < right
            else:
                # all numbers after mid our smaller than mid
                right = mid
                
        return nums[left]
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
                
        result = []
        nums.sort()
        
        # find our a
        for index,num in enumerate(nums):
            if index > 0 and num == nums[index-1]:
                continue
            
            left = index + 1
            right = len(nums) - 1
            
            while left < right:
                threeSum = nums[left] + nums[right] + num
                if threeSum > 0:
                    right -= 1
                elif threeSum < 0:
                    left += 1
                else:
                    result.append([num, nums[left], nums[right]])
                    # update left pointer and avoid left pointer dups 
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                        
        return result

# Time Complexity: O(n²)
# Sorting takes O(n log n).
# Outer loop runs n times, and the two-pointer scan runs O(n) per loop → total O(n²).

# Space Complexity: O(1) auxiliary
# Sorting is in-place, uses constant extra space.
# Output list adds O(k) space for k valid triplets (not counted as auxiliary).
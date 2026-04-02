class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        
        for i, a in enumerate(nums):
            # check if its not te first value in input array and its the same value as before, skip it
            if i > 0 and a == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                left_num = nums[left]
                right_num = nums[right]
                three_sum = a + left_num + right_num

                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    # three_sum equals 0
                    result.append([a, left_num, right_num])
                    
                    left += 1
                    # keep moving left forrward until we reach a non duplicate
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        
        return result
            
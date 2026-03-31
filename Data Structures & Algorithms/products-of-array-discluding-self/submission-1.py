class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # does not count as extra memory
        res = [1] * len(nums)
        
        # intialize prefix
        prefix = 1 
        for i in range(len(nums)):
            res[i] = prefix
            prefix = nums[i] * prefix
            
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] = postfix * res[i]
            # update 
            postfix = nums[i] * postfix
            
        return res

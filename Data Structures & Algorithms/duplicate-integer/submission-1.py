class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if (nums == [] or len(nums) == 1):
            return False
        possible_dups = []
        possible_dups.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] in possible_dups:
                return True
            possible_dups.append(nums[i])
        return False
             
        
         
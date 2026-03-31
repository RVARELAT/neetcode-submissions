class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        complements_dict = {}
        
        for i in range(len(nums)):
            
            complement = target - nums[i]
            
            if complement in complements_dict:
                # we found two numbers that add to target
                return [complements_dict[complement], i]
            else:
                # add num to complemets list
                complements_dict[nums[i]] = i
        
        # should not be reached as we assume pair exists
        return []
        
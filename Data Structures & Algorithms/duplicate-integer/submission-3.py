class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen_nums = set()
        for num in nums:
            if num not in seen_nums:
                seen_nums.add(num)
            else:
                return True
            
        return False
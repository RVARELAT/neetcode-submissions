class Solution:
    # nums is a list of integers passed in and bool is the output
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
             
''' Optimal Solution: 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

🔍 Why This Works:
Set lookup (num in seen) is O(1) on average.
You only make one pass through the list: O(n) time.
You store at most n elements in the seen set: O(n) space.
'''

         
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0

        # keep going until they interest but they interest at beginning
        while True:
            slow = nums[slow]
            # adavce fast twice 
            fast = nums[nums[fast]]
            
            if slow == fast: 
                break

        slow2 = 0 
        # until new slow and slow intersect
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow



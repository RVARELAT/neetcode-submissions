class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # seen to keep track of integers we have seen
        seen = {}
        complement = 0
        # i = the current index (0, 1, 2, 3, …)
        # num = the current element (nums[i])
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            else:
                # store the interger value as the key and index as th value
                seen[num] = i
        # no pairing found so return empty array
        return []
        
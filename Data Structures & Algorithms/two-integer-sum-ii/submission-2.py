class Solution:
    # Given an array of ints numbers and a target int
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers) - 1

        while left < right:
            # move right pointer to the left
            if numbers[left] + numbers[right] > target:
                right -= 1
            # move left pointer to the right
            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                # we add 1 since I used 0-based indexing
                return [left + 1, right + 1]

        return []

# ⏱ Time Complexity
# You start with two pointers: one at the left end, one at the right end.
# In each step of the loop, you either move left one step right or move right one step left.
# That means at most n steps total (each pointer moves at most n times).
# No nested loops.
# ✅ Time Complexity = O(n)

# 💾 Space Complexity
# You only use two integers (left, right) plus the return array of size 2.
# No extra data structures are created.
# ✅ Space Complexity = O(1)
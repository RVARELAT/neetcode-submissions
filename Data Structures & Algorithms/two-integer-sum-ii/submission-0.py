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
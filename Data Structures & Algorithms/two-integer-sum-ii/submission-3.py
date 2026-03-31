class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # make two pointers
        left = 0
        right = len(numbers) - 1
        
        while left < right:
            left_num = numbers[left]
            right_num = numbers[right]
            
            if left_num + right_num == target:
                # add one to indices for off by one issue
                return [left + 1, right + 1]
            
            # if our sum is too big, movr right pointer inward
            elif left_num + right_num > target:
                right -= 1
            
            elif left_num + right_num < target:
                left += 1

        # there will always be one valid soution so this won't be reached
        return []



        
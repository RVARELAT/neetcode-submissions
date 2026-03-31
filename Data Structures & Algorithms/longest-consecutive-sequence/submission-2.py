class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        #Convert the list to a set so duplicates don’t matter.
        num_set = set(nums)
        
    #     Loop through each number, but only start counting when that number is the beginning of a sequence — meaning there’s no num - 1 in the set.


    # From that starting point, walk forward (num + 1, num + 2, …) as long as each next number exists in the set.


    # Keep track of how long that run is.
    # Record the longest length you find.
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                sequence_len = 1
                while num + sequence_len in num_set:
                    sequence_len += 1
                if (sequence_len > max_len):
                    max_len = sequence_len
                
        return max_len
                
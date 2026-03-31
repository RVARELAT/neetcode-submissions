class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequency of each number
        freq = defaultdict(int)      # create a dictionary that defaults to 0
        for num in nums:             # loop through every number in the input list
            freq[num] += 1           # increment the frequency count for that number

        # Step 2: Create buckets where index = frequency
        n = len(nums)                # maximum possible frequency is n
        # buckets = [ [] for _ in range(n + 1) ]   # list of empty lists, size n+1
        buckets = []
        for i in range(n+1):
            buckets.append([])
        
        for num, f in freq.items():     # go through each number and its frequency
            buckets[f].append(num)  # put the number into the bucket for its frequency

        # Step 3: Traverse buckets from highest frequency to lowest
        result = []                     # this will store our top k frequent elements
        for f in range(n, 0, -1):    # go from frequency n down to 1
            # note numtiple numbers can have same frequecy which is why we loop over buckets in list
            for num in buckets[f]:   # for each number in the current frequency bucket
                result.append(num)      # add it to the result list
                if len(result) == k:    # if we already have k elements
                    return result       # return the result immediately
        return result                   # fallback return (shouldn’t normally hit)

# Time and Sapce are O(N)


# 2. The comprehension parts
# A list comprehension has this structure:
# [ expression   for variable in iterable ]
# expression → what you want to put in the list
# variable → a placeholder name for each item in the iterable
# # iterable → something you loop over (like range, a list, etc.)

# 3. In our code
# expression = []
# → we want to put an empty list in each slot
# for _ in range(n+1)
# → loop from 0 up to n, one time per possible frequency
# → _ is a throwaway variable (we don’t care about the actual number, just the count of loops)
# So for n=6 → loop runs 7 times → each time appends [].

# 4. Same thing without comprehension
# You could write it like this instead:
# buckets = []
# for i in range(n+1):
#     buckets.append([])
# That does exactly the same thing — the comprehension is just shorter.


# 1. Why make “buckets”?
# We know how many times each number appears (the freq dictionary).
# Example:
# nums = [1,2,2,3,3,3] →
# freq = {
#   1: 1,   # 1 occurs once
#   2: 2,   # 2 occurs twice
#   3: 3    # 3 occurs three times
# }
# Now we want a way to quickly group numbers by how often they appear.
# That’s what the buckets array does.
# 2. Why size = n + 1?
# n = len(nums) = 6 here.
# The maximum frequency an element can have is n (if all elements are the same).
# So we need buckets for frequencies 0 … n.
# That’s n+1 slots total.
# So:
# buckets = [ [], [], [], [], [], [], [] ]   # 7 empty lists
# index  =    0   1   2   3   4   5   6
# Each index = frequency.
# buckets[1] will hold numbers seen once.
# buckets[2] will hold numbers seen twice.
# … and so on.
# 3. Filling the buckets
# We loop over (num, f) in the freq dictionary:
# num=1, f=1 → put 1 in buckets[1]
# num=2, f=2 → put 2 in buckets[2]
# num=3, f=3 → put 3 in buckets[3]
# Now buckets looks like this:
# [
#  [],        # 0 times (not used)
#  [1],       # appears once
#  [2],       # appears twice
#  [3],       # appears three times
#  [], [], []
# ]
# 4. Why is this useful?
# Now the numbers are organized by frequency.
# If you want the most frequent ones, just walk the array from right to left (biggest frequency → smallest).
# Start at buckets[6] (empty)
# Then buckets[5] (empty)
# Then buckets[4] (empty)
# Then buckets[3] = [3] → top frequent!
# Next buckets[2] = [2] → second most frequent!
# And you stop when you’ve collected k.
# ✅ In plain English:
# Step 2 is just building shelves.
# Each shelf index = “how many times a number shows up.”
# You drop each number on the shelf that matches its count.
# Then later you scan shelves from the fullest side down to pick your top-k.


        

        
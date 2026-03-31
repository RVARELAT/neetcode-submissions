class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash map to keep track of character frequencies in window
        count = {}
        # result of longest substring
        result = 0
        # left pointer for the slidng window
        left = 0
        
        for right in range(len(s)):
            # update our dictionary with character we just saw (if it is not in the dictionary yet, add it to dictionary with a value of 0 + 1)
            count[s[right]] = 1 + count.get(s[right], 0)
            window_len = right - left + 1
            # get the most frequent char value from the window we are in
            max_value = max(count.values())
            # print(max_value)
            
            # we have enough k replacements for that window so make window bigger
            if window_len - max_value <= k:
                if window_len > result:
                    result = window_len
            # make window smaller
            else:
                # make sure to decrement count of character we are removing from window
                count[s[left]] -= 1
                left += 1
        
        return result 

# ✅ Time Complexity (in simple words)
# O(n × m) in the worst case
# But commonly written as O(n) for this problem.
# Why?
# You loop through the string once → n steps
# Inside that loop, you do:
# max(count.values()) → this scans all character counts
# There are at most m unique characters (26 uppercase letters max)
# So worst case:
# For each of n positions, you scan up to m counts → n × m
# Since English uppercase letters are always ≤ 26, we usually treat m as a very small constant.
# So in interview terms it is:
# 👉 O(n) time
# (because 26 is constant, so 26×n behaves like n)

# ✅ Space Complexity (in simple words)
# O(m)
# Why?
# You store a dictionary that keeps:
# one key for each unique character in the window
# at most 26 uppercase letters
# So the dictionary size is m, where m ≤ 26.
# Thus:
# 👉 O(m) space
# 👉 For English letters, this is basically O(1) constant space
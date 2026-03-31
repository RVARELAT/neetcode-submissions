class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # hash map to keep track of character frequencies in window
        count = {}
        # result of longest substring
        result = 0
        # left pointer for the slidng window
        left = 0
        
        for right in range(len(s)):
            # update our dictionary with character we just saw (if it is not in the dictionary yet, add it to distionary with a value of 0 + 1)
            count[s[right]] = 1 + count.get(s[right], 0)
            window_len = right - left + 1
            # get the most frequent char value from the window we are in
            max_value = max(count.values())
            # print(max_value)
            
            # we have enough k replacements for that window so make window bigger
            if window_len - max_value <= k:
                if window_len > result:
                    result = window_len
                right += 1
            # make window smaller
            else:
                # make sure to decrement count of character we are removing from window
                count[s[left]] -= 1
                left += 1
        
        return result 
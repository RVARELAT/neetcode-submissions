class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0
        
        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            # add rifht most character to set
            seen.add(s[right])
            # at this pointt we know our set has no duplicates 
            longest = max(longest, right - left + 1)
        
        return longest
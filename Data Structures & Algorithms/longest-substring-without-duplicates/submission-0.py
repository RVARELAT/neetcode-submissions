class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):
            # If s[right] is already in the window, shrink from the left
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            # Now add the current character
            seen.add(s[right])

            # Update longest window length
            longest = max(longest, right - left + 1)

        return longest
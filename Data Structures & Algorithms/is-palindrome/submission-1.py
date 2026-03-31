class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Case-insensitive → It doesn’t care about uppercase or lowercase letters.
        # Example: "Hello", "HELLO", and "hello" are all treated as the same.
        # Ignores all non-alphanumeric characters → It skips over anything that is not a letter or a number.
        # Alphanumeric = letters (A–Z, a–z) + digits (0–9).
        # Non-alphanumeric = spaces, punctuation, symbols (. , ! ? @ #, etc).
        # Example: "hello!", "he llo", and "he-llo" are all treated as "hello".

        left = 0
        right = len(s) - 1

        while left < right:
            # we check 'while left < right; since we advance pointers in these while loops
            while left < right and s[left].isalnum() == False:
                left += 1
            while left < right and s[right].isalnum() == False:
                right -= 1
            
            # characters are not the same 
            if s[left].lower() != s[right].lower():
                return False
            # advance the pointers
            left += 1
            right -= 1
        
        return True

# 🔎 Time Complexity
# The while left < right: loop moves the two pointers inward.
# Each character in the string is checked at most once (either skipped with isalnum() or compared).
# isalnum() and lower() are constant-time operations, O(1).
# So overall:
# ✅ O(n) time, where n = len(s)

# 🔎 Space Complexity
# You only use two integer variables (left, right) and a few temporary comparisons.
# No extra strings or data structures are built.
# So overall:
# ✅ O(1) space
            
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

            
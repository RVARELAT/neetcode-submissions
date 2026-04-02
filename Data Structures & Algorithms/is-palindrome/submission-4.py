class Solution:
    def isPalindrome(self, s: str) -> bool:
        # remove the spaces and make all lower
        s = "".join(c.lower() for c in s if c.isalnum())
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True 
        
        # s = s.lower()

        # left = 0
        # right = len(s) - 1

        # while left < right:
        #     # isalnum() checks if a string (or character) is made of only letters and numbers.
        #     while left < right and s[left].isalnum() == False:
        #         left += 1
        #     while left < right and s[right].isalnum() == False:
        #         right -= 1

        #     # chars are no the same
        #     if s[left].lower() != s[right].lower():
        #         return False
            
        #     left += 1
        #     right -= 1
        
        # return True
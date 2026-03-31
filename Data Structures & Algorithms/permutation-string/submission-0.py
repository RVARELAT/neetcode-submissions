class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)   
        n2 = len(s2)
        
        # n1 can't be in n2
        if n1 > n2:
            return False
        
        # inializes array fo 26 zero for 26 letters in the alphabet [0, ....... ,0]
        s1_counts = [0] * 26 
        s2_counts = [0] * 26
        
        # loop the len of s1 amount of times
        for i in range(n1):
            # ord of character gets ASCII value of that character (ASCII value of a is 97, b is 98, c is 99, etc)
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        if s1_counts == s2_counts:
            return True

        # we start from index we haven't seen yet to len of n2 - 1
        for i in range(n1, n2):
            # add the character
            s2_counts[ord(s2[i]) - ord('a')] += 1
            # lose the character we just removed from our window
            s2_counts[ord(s2[i - n1]) - ord('a')] -= 1
            if s1_counts == s2_counts:
                return True

        return False

    # Time Complexity: O(n1) + O(n2) = O(n2)
    # Spaxce: O(1)
        
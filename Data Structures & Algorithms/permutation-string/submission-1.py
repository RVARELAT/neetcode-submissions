class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        
        # s1 can't be a substring of s2 if it's longer
        if s1_len > s2_len:
            return False
        
        # intialize array of 26 zeros for 26 letters in the alphabet
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        for i in range(s1_len):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            # build up initial window
            s2_counts[ord(s2[i]) - ord('a')] += 1
            
        if s1_counts == s2_counts:
            return True
        
        # start inclusive at index of n1 
        for i in range(s1_len, s2_len):
            # add the chr we added
            s2_counts[ord(s2[i]) - ord('a')] += 1
            # subtract the char removed from our window
            s2_counts[ord(s2[i - s1_len]) - ord('a')] -= 1
            
            if s1_counts == s2_counts:
                return True
            
        return False
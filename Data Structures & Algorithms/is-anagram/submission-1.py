class Solution:
    def isAnagram(self, s: str, t: str) -> bool:      
        # two strings have diff. lengths
        if len(s) != len(t):
            return False
        
        # Create two hash maps to store character frequencies for each string.
        s_count = {}
        t_count = {}
        
        # we know they are same length here so just iterate through s length
        for i in range(len(s)):
            # "Get the value for key s[i] from the dictionary.
            # If the key doesn't exist, return 0 instead of an error."
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)
            
        if s_count == t_count:
            return True
        
        return False
            
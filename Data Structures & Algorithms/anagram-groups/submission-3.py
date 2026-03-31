class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # default dict sets default value of key to a list
        # This means: If you access a missing key → Python creates it with [].
        res = defaultdict(list) # mapping charCount to List of Anagrams
        
        for s in strs:
            char_count = [0] * 26 # a ... z
            
            for c in s:
                # take ASCII value of char - ASCII value of "a"
                # (value at that index in cunt corresponds to letter)
                char_count[ord(c) - ord("a")] += 1
            
            # list cannot be keys in python so convert count to a tuple
            res[tuple(char_count)].append(s)

        # output expects a list 
        return list(res.values())

# Example of what res looks like 
# {
#  (1,0,0,...): ["eat", "tea", "ate"],
#  (0,1,0,...): ["tan", "nat"],
#  (0,0,1,...): ["bat"]
# }
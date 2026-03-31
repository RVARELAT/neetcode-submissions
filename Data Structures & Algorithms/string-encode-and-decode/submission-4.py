class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
    
        for s in strs:
            encoded_string += str(len(s)) + "#" + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        decoded_string = []
        # pointer 
        i = 0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded_string.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
            
        return decoded_string




# add length of word at the beginning 

# what if word itself has int at beginning

# use # as delimeter

# so do '4#'for length of word and delimter

# take all chars after

# "neet" , "code"

# 4#neet5#code

# O(n) time xomplexity is for both
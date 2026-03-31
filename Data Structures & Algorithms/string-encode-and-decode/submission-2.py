class Solution:

    # join the strings in the list
    def encode(self, strs: List[str]) -> str:
    # use a delimeter with length of next string
        encoding = ""
        for word in strs:
            length = len(word)
            encoding += str(length) + "#" + word 
        return encoding


    # convert the encoding back to list of strings
    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            
            j = i
            
            while s[j] != '#':
                j += 1
            # gets length of word between indices
            length = int(s[i:j])
            
            # make start and end for word 
            start = j + 1
            end = start + length 
            
            # get word and add to list of strings
            word = ""
            while (start < end):
                word += s[start]
                start += 1
            
            i = end
            result.append(word)
            
        return result
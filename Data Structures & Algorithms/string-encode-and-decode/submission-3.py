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


#🕒 Time Complexity

# 🔹 encode
# You loop over every string in strs.
# For each string, you add its length and the word itself to encoding.
# But because Python strings are immutable,
# every time you do encoding += ..., it creates a new copy of the string.
# That means:
# For the 1st word, it copies a few characters.
# For the 2nd word, it copies more.
# And so on — so total work adds up to roughly O(N²) time in the worst case.
# ✅ Time complexity (encode): O(N²)
# (where N = total number of characters across all strings)
# If you used parts = [] and ' '.join(parts) instead, it would become O(N).

# 🔹 decode
# You scan through the entire encoded string once.
# Each loop:
# Finds the # (linear in digits of the number — small)
# Converts the number
# Reads that many characters
# Every character is read exactly once.
# ✅ Time complexity (decode): O(N)

# 💾 Space Complexity

# 🔹 encode
# You build one big string that holds all the characters.
# That string’s size = total number of input characters plus a few for numbers and #.
# ✅ Space complexity (encode): O(N)
# (The new string itself; no big extra data.)

# 🔹 decode
# You build a list of all decoded words.
# That list plus the strings inside it will take about the same amount of space as the original input.
# ✅ Space complexity (decode): O(N)
# (For the output list; only a few integers and counters use extra space.)
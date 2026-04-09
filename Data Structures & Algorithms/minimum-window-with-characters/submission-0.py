class Solution:
    def minWindow(self, s: str, t: str) -> str:
                    
        # want counts to be greater than or equal
        
        # keep hashmap for need and have
            
        # start and end indices as curr result
        
        # pop characters from left until you find one you care about 
        
        # added and removed charcater we did at most 2 operations
        # update one spot on our map and then the have and need
        
        if t == "":
            return ""
        
        countT = {}
        window = {}
        
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
        
        have = 0
        need = len(countT)
        
        res = [-1, -1]
        res_len = float("infinity")
        
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = 1 + window.get(c, 0)
            
            # does this character satisfy the number of characters we need for countT
            if c in countT and window[c] == countT[c]:
                # we just satisfied a condition
                have +=1
                
            # does have == need?
            while have == need:
                # update our result (if its less than curr result length)
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = (right - left + 1)
                # while conditon is met pop from the left of our window
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1  
            
        left, right = res
        
        if res_len != float("infinity"):
            return s[left:right+1]
        else:
            return ""
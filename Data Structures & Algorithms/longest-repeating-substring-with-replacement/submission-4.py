class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # char_count = {}
        # result = 0
        
        # left = 0
        # for right in range(len(s)):
        #     char_count[s[right]] = 1 + char_count.get(s[right], 0)
            
        #     # window size - most frequent  > k means window is not valid
        #     while (right - left + 1) - max(char_count.values()) > k:
        #         # update char freuquency
        #         char_count[s[left]] -= 1
        #         # move left pointer forward
        #         left += 1
                
        #     result = max(result, right - left + 1)
            
        # return result

    # optimized way, time is O(n) not O(26 * n)
        char_count = {}
        result = 0
        
        left = 0
        max_frequency = 0
        
        for right in range(len(s)):
            char_count[s[right]] = 1 + char_count.get(s[right], 0)
            # update max frequency right away, compare with char frequency we just updated
            max_frequency = max(max_frequency, char_count[s[right]])
            # window size - most frequent  > k means window is not valid
            while (right - left + 1) - max_frequency > k:
                # update char freuquency
                char_count[s[left]] -= 1
                # move left pointer forward
                left += 1
                
            result = max(result, right - left + 1)
            
        return result

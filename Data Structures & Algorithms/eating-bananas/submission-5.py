class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # set pointers
        # from 1 ... max of piles
        left = 1
        right = max(piles)
        # result
        smallest_k = right
        
        while left <= right:
            mid = (left + right) // 2
            # calculator hours it would take if we used this mid (k)
            hours = 0
            
            for pile in piles:
                hours += math.ceil(pile/mid)
                
            if hours <= h:
                smallest_k = min(smallest_k, mid)
                # seach left side
                right = mid - 1
            # search right side
            else:
                left = mid + 1
        
        # stop and return result
        return smallest_k
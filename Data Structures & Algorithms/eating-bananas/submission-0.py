class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Step 1: define search range for k
        # smallest possible speed = ?
        # largest possible speed = ?
        left = 1
        right = max(piles)
        
        # Step 2: binary search for the smallest valid k
        while left <= right:
            mid = (left + right) // 2 # candidate eating speed
            
            # Step 3: calculate total hours needed with this speed
            total_hours = 0
            for pile in piles:
                # use ceiling division to find how many hours this pile takes
                total_hours += math.ceil(pile / mid)
                
            # Step 4: check if Koko can finish in time
            if total_hours <= h:
                # she can finish → maybe try slower speed
                right = mid - 1
            else:
                # she cannot finish → needs faster speed
                left = mid + 1
        
        # Step 5: return the smallest k found
        return left 
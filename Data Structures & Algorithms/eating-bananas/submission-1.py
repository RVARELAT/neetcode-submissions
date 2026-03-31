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


# ⏱ Time Complexity: O(n × log M)
# n = number of piles
# M = size of the largest pile
# Here’s why:
# The binary search tries different eating speeds k between 1 and max(piles) — that range has about log M possible midpoints (because binary search halves it each time).
# For each speed, you go through all piles once to calculate total hours → that’s O(n).
# Multiply them: O(n × log M)
# ✅ In simple words:
# You test a few (log M) possible speeds, and each test checks all piles once.

# 💾 Space Complexity: O(1)
# You only use a few variables (left, right, mid, total_hours) — no extra lists or data structures.
# ✅ In simple words:
# It doesn’t store anything big — it just reuses a few numbers while looping.


# 🔹 What happens at the end
# When the while loop stops, the pointers have crossed:
# right < left.

# At that point:
# right points to the last speed that failed (too slow),
# left points to the first speed that worked (just fast enough).
# And since we want the minimum valid speed,

# ✅ the correct answer is left.
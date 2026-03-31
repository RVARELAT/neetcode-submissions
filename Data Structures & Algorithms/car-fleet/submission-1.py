class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            # array of pairs
        pair = [[p, s] for p, s in zip(position, speed)]
        # will tell us how many car fleets we have at the end
        stack = [] 
        
        for p,s in sorted(pair)[::-1]: # reverse sorted order
            # get the time of car it will take to reach the end and append it to the stack
            stack.append((target - p) / s)
            # two cars on stack collide
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # pops the car before the car ahead of it
        
        return len(stack)

# ⏱ Time Complexity (simple words)
# Let n = number of cars.
# Main steps:
# Build pair list
# pair = [[p, s] for p, s in zip(position, speed)]
# We loop through all cars once → O(n) time.
# Sort pair
# sorted(pair)
# Sorting n items takes O(n log n) time.
# Loop through sorted list
# for p, s in sorted(pair)[::-1]:
#     ...
# We visit each car once, do constant work (append, compare, maybe pop) → O(n) time.
# Total time:
# The slowest part is the sort: O(n log n)
# Other loops are O(n) which is smaller than O(n log n) for large n
# So overall time complexity:
# 👉 O(n log n)
# In simple words:
# Time grows a bit more than linearly because we have to sort the cars.

# 🧮 Space Complexity (simple words)
# Extra memory we use:
# pair list
# Stores [position, speed] for each car.
# Size is n → O(n) space.
# stack list
# In the worst case, no car catches up, so every car is its own fleet.
# Then stack holds n times → O(n) space.
# So total extra space:
# pair → O(n)
# stack → O(n)
# O(n) + O(n) is still O(n)
# 👉 Space complexity: O(n)
# In simple words:
# The memory we use grows in direct proportion to the number of cars.
    
    

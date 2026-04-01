class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # create array of pairs 
        pair = [[p, s] for p,s in zip(position,speed)]
        
        # will tell us how many car fleets we have at the end
        stack = []
        for p,s in sorted(pair)[::-1]: # revrse sorted order
            # what time it will reach destination (using decimal devision)
            stack.append((target - p) / s)
            # does it overlap with other at the top of our stack
            # check if one before reaches destination (remember we iteratre through array in reverse order)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        
        return len(stack)

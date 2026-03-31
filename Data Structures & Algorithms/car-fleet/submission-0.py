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
    
    
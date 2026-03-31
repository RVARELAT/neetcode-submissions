class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack, strictly decreasing temps in this case 
        stack = []
        result = [0] * len(temperatures)
        
        for i, temperature in enumerate(temperatures):
            # check if curr temp is warmer than top of stack
            while stack != [] and temperature > stack[-1][0]:
                # next greater index value (current index value) - stack index
                stack_temp, stack_temp_index = stack.pop()
                result[stack_temp_index] = i - stack_temp_index
                #stack.append((temperature, i))

            # add (value, curr index) to stack?
            stack.append((temperature, i))
        
        return result
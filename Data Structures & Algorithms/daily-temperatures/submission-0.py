class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
            # temp and index temperature occured at
        stack = [] # pair: [temp, index]
        result = [0] * len(temperatures)
        
        for i, t in enumerate(temperatures):
            # compare num to top of the stack
            while stack != [] and t > stack[-1][0]:
                # pop top from stack
                stack_temp, stack_ind = stack.pop()
                # add distance to our result
                result[stack_ind] = i - stack_ind
            stack.append([t, i])
                
        return result

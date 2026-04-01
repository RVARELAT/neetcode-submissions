class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = [] # pair: (index, height)

        # stak will contain current heights that we are considering and will pop them from the top
            
        for i, h in enumerate(heights):
            # we dont know if we can extrant start backwards just yet
            start = i
            # pop from stack since prev height is greater
            while stack != [] and stack[-1][1] > h:
                index, height = stack.pop()
                maxArea = max(maxArea, height * (i - index))
                # extend start index backwards to index we just popped since its height was greater
                start = index 
            # add it to stack
            stack.append((start, h))
            
        # might still have entries and we can extend them to end of histogram
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))
        
        return maxArea
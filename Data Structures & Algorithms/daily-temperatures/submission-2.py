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


# ⏱ Time Complexity (O(n)) – simple words
# We loop through the array once: for i, t in enumerate(temperatures)
# Each index is:
# pushed to the stack once
# and popped at most once
# So total operations are proportional to n, not n².
# 👉 Even though there’s a while loop, the total number of pops across the whole run is still at most n.
# So:
# Time = O(n)

# 📦 Space Complexity (O(n)) – simple words
# We use:
# result → an array of size n
# stack → in the worst case, we could push all days onto the stack (e.g., strictly decreasing temperatures)
# So the stack can hold up to n elements.
# Total extra space:
# Space = O(n)  # for result + stack
# (If we don’t count the output result as “extra”, then the extra space is O(n) for the stack alone.)


# Rule 2: Output space is usually not counted
# When the output must be size n, like in this problem:
# result is unavoidable — every valid solution needs it.
# So sometimes we say the extra space is O(n) (just the stack).
# If we include result, total space is still:
# O(n)  # not O(2n)
# because of rule #1.

# ⭐ Final Summary (for your notes)
# The algorithm stores a result array of size n and a stack of size up to n.
# That is 2n actual memory, but Big-O ignores constant factors.
# So 2n → O(n).
# Big-O measures growth, not exact counts.

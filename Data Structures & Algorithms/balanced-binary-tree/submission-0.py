# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # make as list since python has issue with global variables
        balanced = [True]

        def height(root):
            if root is None:
                return 0

            left_height = height(root.left)
            # we found imbalance on the left
            if balanced[0] is False:
                return 0
            right_height = height(root.right)

            if abs(left_height - right_height) > 1:
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)

        height(root)
        return balanced[0]

# ⏱ Time Complexity
# Let n = number of nodes in the tree.
# What happens:
# Each node is visited once by height(root):
# You compute left height
# You compute right height
# You do a constant amount of work (a few ifs and max)
# Even though there is an early-return optimization if balanced[0] is False, in the worst case (the tree is balanced) you still visit every node exactly once.
# So:
# ✅ Time complexity: O(n)
# In simple words:
# The work grows linearly with the number of nodes, because you touch every node one time.



# 🧠 Space Complexity
# This is recursion, so space comes from the call stack.
# Let h = height of the tree.
# At most, your recursion goes down from the root to the deepest leaf → that’s h calls on the stack.
# There’s also the balanced list (size 1) which is O(1) space.
# So:
# Space from recursion = O(h)
# In terms of n:
# Best / typical (balanced tree):
# height h ≈ log n → space = O(log n)
# Worst case (totally skewed tree, like a linked list):
# height h = n → space = O(n)
# So the usual answer:
# ✅ Space complexity: O(h), which is O(n) in the worst case.
        
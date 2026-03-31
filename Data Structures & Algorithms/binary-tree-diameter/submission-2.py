# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_diameter = [0]

        # helper function to find the height of a root
        def height(root):
            if root is None:
                return 0
            
            height_left = height(root.left)
            height_right = height(root.right)

            diameter = height_left + height_right
            largest_diameter[0] = max(largest_diameter[0], diameter)

            return 1 + max(height_left, height_right)

        height(root)
        return largest_diameter[0]

# ⏱ Time Complexity → O(n)
# Where n = number of nodes.
# Why?
# Every node is visited once.
# At each node we do:
# compute left height
# compute right height
# update a number
# All of these are constant-time operations per node.
# So total work:
# n nodes × constant work = O(n)

# 🧠 Space Complexity → O(h)
# h = height of the tree
# This comes from recursion depth:
# The recursion stack stores one frame per level of the tree.
# In the best case (balanced tree): height = log n → space = O(log n)
# In the worst case (linked-list shaped): height = n → space = O(n)
# Since LeetCode wants the worst-case complexity:
# ➡️ Space = O(n) in the worst case
# ➡️ Space = O(log n) in a balanced tree
# No extra data structures besides a tiny list [0] are used.
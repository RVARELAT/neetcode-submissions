# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None
        
        if root != None:
            # swap children values
            temp = root.left
            root.left = root.right
            root.right = temp

            self.invertTree(root.left)
            self.invertTree(root.right)
        
        return root


# ⏱️ Time Complexity: O(n)
# n = number of nodes in the tree.
# Why?
# Your function:
# Visits every single node once
# Swaps its left and right child (constant-time work)
# Recursively calls itself on the left subtree and the right subtree

# 🧠 Space Complexity: O(h)
# h = height of the tree (max depth of recursion)
# Why?
# This is recursion, so:
# Each recursive call is stored on the call stack.
# Worst-case height = number of nodes in a long chain.
# Two main cases:
# ✔️ Best case (balanced tree)
# Height = log n
# Space = O(log n)
# ❌ Worst case (skewed tree: like a linked list)
# Height = n
# Space = O(n)
# So the space complexity is:
# ➡️ O(h) where h is tree height
# ➡️ Worst-case: O(n)
# ➡️ Balanced-case: O(log n)
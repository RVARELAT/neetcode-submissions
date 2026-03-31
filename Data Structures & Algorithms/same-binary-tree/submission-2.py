# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def same(p, q):
            if p == None and q == None:
                return True
            if (p != None and q == None) or (p == None and q != None):
                return False
            # check if values are equal
            if p.val != q.val:
                return False

            return same(p.left, q.left) and same(p.right, q.right)

        return same(p, q)

      
# ⏱️ Time Complexity: O(n)
# Where n = number of nodes across the trees (they will be the same size if identical).
# Why?
# You visit each node once.
# Each visit does constant work: comparing values and doing two recursive calls.
# So total work = O(n).

# 💾 Space Complexity: O(h)
# Where h = height of the tree.
# Why? Because recursion builds a call stack as deep as the tree.
# Best case (perfectly balanced tree)
# Height = log n
# Space = O(log n)
# Worst case (linked-list shaped tree)
# Height = n
# Space = O(n)
# Since the tree can be skewed, the worst-case space complexity is:
# ➡️ O(n)
        
        
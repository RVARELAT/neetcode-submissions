# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # depth is 0
        if root is None:
            return 0

        if root != None:
            max_left = 1 + self.maxDepth(root.left)
            max_right = 1 + self.maxDepth(root.right)

        return max(max_left , max_right)

# ⏱️ Time Complexity: O(n)
# Where n = number of nodes.
# Why?
# You visit every node exactly once.
# At each node, you do a tiny constant amount of work (check left/right, return max).
# So total work:
# Node 1 → constant work
# Node 2 → constant work
# Node 3 → constant work
# ...
# Node n → constant work
# ➡️ O(n) time.

# 🧠 Space Complexity: O(h)
# Where h = the height of the tree (depth of the recursion calls).
# Why?
# Each recursive call is added to the call stack until it returns.
# In the worst case, the tree is a straight line (like a linked list), so height = n.
# In the best case, the tree is balanced, so height = log n.
# Two scenarios:
# ✔️ Balanced tree
# Height = log n
# Space = O(log n)
# ❌ Skewed tree
# Height = n
# Space = O(n)
# Because the problem allows up to 100 nodes and doesn’t guarantee balance, the recommended answer is:
# ➡️ O(n) space in the worst case
# ➡️ Recursion call stack stores up to n nodes 
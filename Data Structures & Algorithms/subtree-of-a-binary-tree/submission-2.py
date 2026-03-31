# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # empty tree is a subtree of any tree
        if subRoot is None:
            return True
        # if tree is empty, subroot cannot be a substree of Tree
        if root is None:
            return False

        # at this point we know both trees are not empty
        if self.sameTree(root, subRoot) == True:
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        
    # helper functin
    def sameTree(self, s, t):
        # both trees are empty 
        if s is None and t is None:
            return True

        # both trees are not empty and root is the same we actually compare the Trees
        if (s != None and t != None) and s.val == t.val:
            # We want to know if left subtrees are the same
            # we want to know if the right subtrees are the same
            return self.sameTree(s.left, t.left) and self.sameTree(s.right, t.right)

        # if none of if statements execute, then one of trees is empty and other is nonempty 
        return False

# ⏱ **Time Complexity (Simple Explanation)**

# Let:

# - `n` = number of nodes in `root`
# - `m` = number of nodes in `subRoot`

# ### **Worst Case**

# For every node in `root`, we may compare up to **all** nodes of `subRoot`.

# So the worst-case time is:

# ```
# O(n * m)
# ```

# Why?

# - The `isSubtree` function visits each of the `n` nodes.
# - For each visit, `sameTree` may compare up to `m` nodes.

# This is acceptable because constraints are small (max 100 nodes each).

# ---

# # 🧠 **Space Complexity (Simple Explanation)**

# ### **Space comes from recursion depth.**

# Worst-case heights:

# - `root` height = `O(n)` (if skewed)
# - `subRoot` height = `O(m)`

# Recursive stack could go that deep.

# So total space:

# ```
# O(n + m)
# ```

# This is because:

# - `isSubtree` recursion can go `n` levels deep
# - `sameTree` recursion can go `m` levels deep

# We add them because they can be nested.

        
        
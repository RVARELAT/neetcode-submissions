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

        # if p is None and q is None:
        #     return True

        # def traverse(root1, root2):
        #     if (root1 is None and root2 != None):
        #         return False
        #     if (root1 != None and root2 is None):
        #         #print("YOPPOPPPPPP")
        #         return False
            
        #     if (root1 is None and root2 is None):
        #         pass
        #     elif (root1.val == root2.val):
        #         traverse(root1.left, root2.left)
        #         traverse(root1.right, root2.right)
        #         #return True
        #     else:
        #         return False

        # if (traverse(p, q) == False):
        #     return False
        # else: 
        #     return True
        # #return traverse(p, q)



        
        
        
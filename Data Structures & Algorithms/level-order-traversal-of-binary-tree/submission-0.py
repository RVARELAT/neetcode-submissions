# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Tree is empty
        if root is None:
            return []
        
        queue = deque([root])
        result = []
        
        # queue.append(value)   # add to back
        # queue.popleft()       # remove from front
        
        while queue:
            level = []
            level_size = len(queue)
            
            for _ in range(level_size):
                # remove one node
                popped_node = queue.popleft()
                # add its value to the level
                level.append(popped_node.val)
                # add its children to queue
                if popped_node.left is not None:
                    queue.append(popped_node.left)
                if popped_node.right is not None:
                    queue.append(popped_node.right)
        
            result.append(level)
            
        
        return result
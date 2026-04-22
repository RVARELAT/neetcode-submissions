"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Hashmap
        oldToCopy = {None : None}

        cur = head 
        while cur != None:
            # create a deep copy of this node
            copy = Node(cur.val)
            # Take this copy and put it in our hashmap
            oldToCopy[cur] = copy
            cur = cur.next

        # now we set the pointers
        cur = head
        while cur != None:

            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]



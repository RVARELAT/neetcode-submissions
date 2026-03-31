# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        # find the length of the linked list
        curr = head
        length = 0
        while curr != None:
            length += 1
            curr = curr.next

        # find the node we want to remove
        prev = head
        curr = head
        new_n = (length - n)

        for i in range(new_n):
            # start moving prev after we have moved curr forward once
            if (i == 0):
                curr = curr.next
                continue
            prev = prev.next
            curr = curr.next
        
        # node to remove is head, so we can just move head forward
        if (new_n == 0):
            head = head.next
            return head

        # remove node
        prev.next = curr.next

        return head

        

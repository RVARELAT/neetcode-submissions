# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
            if (i == 0):
                curr = curr.next
                continue 
            
            prev = prev.next
            curr = curr.next
            
        # node to remove is heaf
        if new_n == 0:
            head = curr.next
            return head
        
        prev.next = curr.next
        
        return head

            

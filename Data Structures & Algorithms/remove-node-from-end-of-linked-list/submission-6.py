# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head 
        length = 0
        
        # dont care about value
        dummy = ListNode(0, head)
        # start at dummy so we can easily handle the node to remove
        left = dummy
        right = head 
				
				# start right pointer from N node
        while n > 0 and right != None:
            right = right.next
            n -= 1

        while right != None:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
            

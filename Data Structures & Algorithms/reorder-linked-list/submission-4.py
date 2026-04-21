# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half of the list

        # second half of the list
        second = slow.next
        # This will be the final node
        slow.next = None
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # mrge two halfs

        # prev is the head of the second half
        second = prev

        # first is the head of the first half
        first = head

        
        # mrge two halfs

        # Since second half can be shorter
        while second:
            temp1 = first.next
            temp2 = second.next

            # entering second node between first and first.next
            first.next = second 
            second.next = temp1

            first = temp1
            second = temp2



        
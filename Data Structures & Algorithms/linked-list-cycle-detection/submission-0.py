# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a two pointer approach
        # The slow pointer moves one step at a time, while the fast pointer moves two steps at a time. 
        slow_pointer = head
        fast_pointer = head

        # fast reaches linked list before slow does and fast nes tells us if next part of list is empty
        while fast_pointer != None and fast_pointer.next != None:

            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            # cycle has been found as fast pointer caught up to slow pointer
            if slow_pointer == fast_pointer:
                return True

        # no cycle found
        return False

    
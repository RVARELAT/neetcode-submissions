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

        
# ✅ Time Complexity (Simple Words)
# Time = O(N)
# Why?
# First loop: you walk through the whole list once → O(N)
# Second loop: you walk part of the list again → at worst O(N)
# Add them together:
# O(N) + O(N) = O(N)
# We ignore constants, so final answer is O(N).
# In simple terms:
# 👉 You scan the list twice, but scanning twice is still “linear time.”

# ✅ Space Complexity (Simple Words)
# Space = O(1)
# Why?
# You only use a few pointer variables (curr, prev, head), no extra data structures, no arrays — nothing grows with the size of the list.
# In simple words:
# 👉 You don’t create anything big. Just a few pointers.

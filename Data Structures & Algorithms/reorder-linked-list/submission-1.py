# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # empty lists or lists with 1 node
        if head is None or head.next is None:
            return
    
        # SPLIT up list into two halves
        
        # slow pointer will be at halfway point
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        # second half of the list
        list2_head = slow.next
        # first half of the list
        list1_head = head
        # THIS ACUTALLY SPLITS LIST 1 FROM LIST 2
        slow.next = None

        # REVERSE second half of list 
        
        curr = list2_head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # new list 2 head after reversing list 2
        list2_head = prev
        
        # now lets MERGE list 1 and list 2 for proper ordering:
        
        while list1_head != None and list2_head != None:
            temp1 = list1_head.next
            temp2 = list2_head.next
            
            list1_head.next = list2_head
            list2_head.next = temp1
            list2_head = temp2
            list1_head = temp1


# ✅ TIME COMPLEXITY — O(n)
# We walk through the list a constant number of times, and each pass touches each node only once.
# Breakdown:
# Finding the middle (slow & fast pointers)
# The while fast != None loop moves through the list once.
# This takes O(n) time.
# Reversing the second half
# The reverse loop also touches each node exactly once.
# This takes O(n/2) → still O(n).
# Merging the two halves
# We again touch each node once during merging.
# This is O(n).
# Combine them:
# O(n) + O(n) + O(n) = O(n)
# So the total time complexity is:
# ⭐ O(n)
# Because we're only making a few passes over the list.

# ✅ SPACE COMPLEXITY — O(1)
# We are not creating any new lists, arrays, or data structures.
# We only use a few pointer variables:
# slow
# fast
# curr
# prev
# temp1, temp2
# maybe 1–2 other small variables
# No matter how big the linked list is, we always use the same small, constant amount of extra space.
# So:
# ⭐ O(1) space


        
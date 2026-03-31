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

# 🚀 Time Complexity — O(n) (Simple Words)
# Each pointer moves through the list.
# Slow moves 1 step at a time.
# Fast moves 2 steps at a time.
# Even though fast moves faster, both pointers will never visit more than O(n) nodes total.
# Worst case:
# They either meet inside the cycle
# Or the fast pointer reaches the end
# So total work is:
# 👉 O(n)
# (where n = number of nodes in the list)


# 🚀 Space Complexity — O(1) (Simple Words)
# We only use two pointers:
# slow_pointer
# fast_pointer
# We don’t:
# create new nodes
# use a hashset
# use recursion
# store visited nodes
# So the space usage stays constant:
# 👉 O(1) extra space
    
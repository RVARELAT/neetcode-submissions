# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy 

        # 1 -> 2 -> 3
        # need a pointer to the number 1 so we can do 1.next point to 3
        # 1 -> 3 -> 2

        while True:
            kth = self.getKth(groupPrev, k)
            # not enough nodes in group so dont reverse them
            if kth == None:
                break 
            groupNext = kth.next

            # reverse group
            prev = kth.next
            curr = groupPrev.next

            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next


    def getKth(self, curr, k):
        while curr is not None and k > 0:
            curr = curr.next
            k -= 1
        return curr
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        cur = dummy 

        carry = 0

        while l1 != None or l2 != None or carry != 0:
            # get the value from the node in l1
            if l1 != None:
                v1 = l1.val
            else:
                v1 = 0
            # get the value from the node in l2
            if l2 != None:
                v2 = l2.val
            else:
                v2 = 0

            # compoute new digit
            val = v1 + v2 + carry
            # now we can have a new carry
            carry = val // 10
            # so we get the ons place value after striing the carry part 
            val = val % 10
            # create this new node
            cur.next = ListNode(val)
            
            # update pointers
            cur = cur.next

            if l1 != None:
                l1 = l1.next
            else:
                l1 = None

            if l2 != None:
                l2 = l2.next
            else:
                l2 = None

        return dummy.next



# ⭐ Summary for Notes (Copy/Paste)
# Idea:
# Add digits from each list one at a time, just like adding numbers on paper. Use a carry to hold overflow above 9, create a new node for each digit of the result, and move forward through both lists until all digits and the carry are processed.
# Time Complexity:
# O(m + n) — you visit each node in both input lists exactly once.
# Space Complexity:
# O(1) extra space (only uses a few pointers and integers)
# O(max(m, n)) total space if counting the new result list


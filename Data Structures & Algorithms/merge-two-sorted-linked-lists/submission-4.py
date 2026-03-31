# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy 

        while list1 != None and list2 != None:
            # list 2 value is greater
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            # list 2 value is less than or equal
            else:
                tail.next = list2
                list2 = list2.next
            # update tail pointer
            tail = tail.next
        
        # case where list 1 is empty and list 2 is not
        if list1 == None:
            # connect rest of list to list 2
            tail.next = list2
        # case where list 2 is empty and list 1 is not
        else:
            # cpnnect rest of list to list 1
            tail.next = list1

        return dummy.next
        
# ✅ Time Complexity (Simple Words)
# O(n + m)
# We visit each node in list1 exactly once → n steps
# We visit each node in list2 exactly once → m steps
# Every step does a constant amount of work (compare values, move pointer)
# So total work is:
# n + m operations → O(n + m)
# This is optimal — we must look at every node at least once.

# ✅ Space Complexity (Simple Words)
# O(1) extra space
# We only use:
# dummy
# tail
# two pointers (list1, list2)
# No arrays, no new copies of nodes, no recursion.
# We reuse the nodes from the original lists.
# So the space does not grow with input size.
        
        
        
        
        
# my way is wrong  
        
        # # handle empty list cases first
        # if list1 == []:
        #     return list2
        # if list2 == []:
        #     return list1

        # # head of list 1
        # curr1 = list1
        # # head of list 2
        # curr2 = list2

        # # compare values of heads for new head
        # # head of list 2 is new head
        # if curr1.val >= curr2.val:
        #     new_list = curr2
        # # head of list 1 is new head
        # else:
        #     new_list = curr1

        # while curr1 != None and curr2 != None:
        #     # compare values using curr pointers
        #     # list 1 val is greater than list 2 val
        #     if curr1.val >= curr2.val:
        #         temp = curr2.next
        #         curr2.next = curr1
        #         curr2 = temp
        #         curr1 = curr1.next
        #     # list 2 val is greater than list 1 val
        #     else:
        #         temp = curr1.next
        #         curr1.next = curr2
        #         curr1 = temp
        #         curr2 = curr2.next

        # return new_list

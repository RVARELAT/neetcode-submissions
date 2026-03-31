# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to start building the merged list
        dummy = ListNode(-1)  
        current = dummy   # Pointer to build the new list
        
        # While both lists are not empty
        while list1 != None and list2 != None:
            # Compare the values at list1 and list2
            # Attach the smaller one to current.next
            # Move the pointer in that list forward
            #print(list1.val, " ", list2.val)
            if list1.val <= list2.val:
                #print("HI")
                current.next = list1
                current = current.next
                #print(current.next.val)
                list1 = list1.next
            else:
                current.next = list2
                current = current.next
                list2 = list2.next

        # After the loop, at least one list is empty
        # Attach the remaining non-empty list
        if list1 == None:
            current.next = list2
        else:
            current.next = list1

        
        # Return the merged list (dummy.next skips the placeholder)
        #print("Current.next:", current.next.val)
        return dummy.next
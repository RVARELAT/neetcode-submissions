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

# Time Complexity

# You’re traversing both linked lists exactly once. Each step moves forward either in list1 or list2.
# In total, you’ll make n + m steps, where
# n = length of list1
# m = length of list2
# ✅ Time Complexity = O(n + m)

# Space Complexity

# You’re not creating any new nodes — you’re just re-linking the existing ones.
# The only extra space used is:
# The dummy node (constant space).
# A few pointers (current, list1, list2).
# ✅ Space Complexity = O(1) (constant extra space)

# 👉 So your solution is optimal:
# Time: O(n + m)
# Space: O(1)
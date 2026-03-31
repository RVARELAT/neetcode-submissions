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
    
        # split up list into two halves
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

        # reverse second half of list 
        curr = list2_head
        prev = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # new list 2 head after reversing list 2
        list2_head = prev
        
        # now lets combine list 1 and list 2 for proper ordering:
        while list1_head != None and list2_head != None:
            temp1 = list1_head.next
            temp2 = list2_head.next
            
            list1_head.next = list2_head
            list2_head.next = temp1
            list2_head = temp2
            list1_head = temp1
            


        
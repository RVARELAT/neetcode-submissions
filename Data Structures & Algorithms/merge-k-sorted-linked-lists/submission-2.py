# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        heap = []

        # Dummy node makes it easier to build the result list.
        dummy_node = ListNode(-1)
        result = dummy_node

        # Put the first node from each non-empty list into the heap.
        for i, head in enumerate(lists):
            if head is not None:
                # (node value, list index, actual node)
                heapq.heappush(heap, (head.val, i, head))

        while heap:
            # Get the smallest available node.
            value, i, node = heapq.heappop(heap)

            # Attach it to the merged list.
            result.next = node
            result = result.next

            # If this list still has another node,
            # reveal that next node by pushing it into the heap.
            if node.next is not None:
                heapq.heappush(
                    heap,
                    (node.next.val, i, node.next)
                )

        return dummy_node.next
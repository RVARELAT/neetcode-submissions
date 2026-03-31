class Node:
    def __init__(self, val):
        # every node has a value and a pointer to next node
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        # pointer to the head
        self.head = None
        self.size = 0
    
    def get(self, index: int) -> int:
        # index is out of bounds
        if (index < 0) or (index >= self.size):
            return -1

        # if list is empty
        if self.size == 0:
            return -1
        
        curr_node = self.head
        while index != 0:
            curr_node = curr_node.next
            index -= 1
        
        return curr_node.val

    
    def insertHead(self, val: int) -> None:
        # if list is empty
        if self.size == 0:
            new_node = Node(val)
            self.head = new_node
            self.size += 1
            return

        # list is not empty
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

        
    def insertTail(self, val: int) -> None:
        new_node = Node(val)
        # if lists is empty 
        if self.size == 0:
          self.head = new_node
          self.size += 1 
          return
          
        curr_node = self.head
        while curr_node.next != None:
            curr_node = curr_node.next
            
        curr_node.next = new_node
        self.size += 1
        
        
    def remove(self, index: int) -> bool:
        if (index < 0) or (index >= self.size):
            return False
        
        # remove the head
        if (index == 0):
            self.head = self.head.next
            self.size -= 1
            return True
            
        prev_node = None
        curr_node = self.head
        while index != 0:
            prev_node = curr_node
            curr_node = curr_node.next
            index -= 1
            
        # we have found the node to remove
        prev_node.next = curr_node.next
        self.size -= 1
        return True
    
    def getValues(self) -> List[int]:
        values_arr = []
        curr_node = self.head
        while curr_node != None:
            values_arr.append(curr_node.val)
            curr_node = curr_node.next
            
        return values_arr
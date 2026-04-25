class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key to node

        self.left = Node(0, 0)
        self.right = Node(0, 0)
        
        # Left = least recently used, right = most recent
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from left 
    def remove(self, node):
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    # insert node from right
    def insert(self, node):
        prev = self.right.prev
        next = self.right

        prev.next = node
        next.prev = node

        node.next = next
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        # insert it in our hashmap
        self.cache[key] = Node(key, value)

        # insert it intoo ourlist
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            # remove from the list and delete LRU from the hashmap
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    

        

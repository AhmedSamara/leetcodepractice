class Node:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.contents = {}

        # dummy head/tail so everything is real.
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_front(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.contents:
            return -1

        # move node to front because it was accessed.
        node = self.contents[key]
        self._remove(node)
        self._add_to_front(node)
        return node.value
        
    def put(self, key: int, value: int) -> None:
        # if it exists, update lru.
        if key in self.contents:
            node = self.contents[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
            return

        # evict the node before the tail (last used) if needed.
        if len(self.contents) >= self.capacity:

            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.contents[lru_node.key]

        new_node = Node(key, value)
        self._add_to_front(new_node)
        self.contents[key] = new_node


        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

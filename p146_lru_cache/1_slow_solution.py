# thoughts:
# - spec didn't specify LRU must update on get, but expected to know from linked wiki.
# - confused myself with using min or max lru.
# - this solution is slow.

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.contents = {}
        self.lru = {}

    def updateLRU(self, key):
        for i in self.lru:
            self.lru[i] += 1
        self.lru[key] = 0
        

    def get(self, key: int) -> int:
        if key in self.contents:
            self.updateLRU(key)
            return self.contents[key]
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        # if it exists, update lru.
        if key in self.contents:
            self.contents[key] = value
            self.updateLRU(key)
            return

        # if new, add to contents.
        if len(self.contents) < self.capacity:
            self.contents[key] = value
            self.updateLRU(key)
        else:
            # find lowest index and evict
            i = max(self.lru, key=self.lru.get)
            del self.lru[i]
            del self.contents[i]
            self.contents[key] = value
            self.updateLRU(key)

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node: 
    def __init__(self, key, value): 
        self.nxt = self.prev = None
        self.value = value
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.right = Node(0,0)
        self.left = Node(0,0)
        self.left.nxt, self.right.prev = self.right, self.left

        self.cap = capacity
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1 

    def remove(self, node): 
        prev, nxt = node.prev, node.nxt
        prev.nxt, nxt.prev = nxt, prev

    def insert(self, node): 
        prev, nxt = self.right.prev, self.right
        prev.nxt = nxt.prev = node
        node.nxt, node.prev = nxt, prev

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap: 
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}   # key -> Node

        # Dummy nodes
        self.left = Node(0, 0)    # LRU side
        self.right = Node(0, 0)   # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove node from wherever it currently is
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert node immediately before right (MRU position)
    def insert(self, node):
        prev = self.right.prev

        prev.next = node
        node.prev = prev

        node.next = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Accessing it makes it most recently used
        self.remove(node)
        self.insert(node)

        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Remove old node
            self.remove(self.cache[key])

        # Create new/updated node
        node = Node(key, value)
        self.cache[key] = node

        # Put at MRU
        self.insert(node)

        # Too many items → remove LRU
        if len(self.cache) > self.capacity:
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]
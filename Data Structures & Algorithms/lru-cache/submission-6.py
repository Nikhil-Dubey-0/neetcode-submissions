class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.mapping = {}
        self.capacity = capacity
        self.first = None
        self.last = None

    def get(self, key: int) -> int:
        if key not in self.mapping:
            return -1

        node = self.mapping[key]

        # Already MRU
        if node != self.last:

            # Remove node from current position
            if node.prev:
                node.prev.next = node.next
            else:
                # node was first
                self.first = node.next

            if node.next:
                node.next.prev = node.prev

            # Put node at MRU
            node.prev = self.last
            node.next = None

            self.last.next = node
            self.last = node

        return node.value

    def put(self, key: int, value: int) -> None:

        # Existing key
        if key in self.mapping:
            node = self.mapping[key]
            node.value = value

            # Move it to MRU
            if node != self.last:

                if node.prev:
                    node.prev.next = node.next
                else:
                    self.first = node.next

                if node.next:
                    node.next.prev = node.prev

                node.prev = self.last
                node.next = None
                self.last.next = node
                self.last = node

            return

        # New node
        node = Node(key, value)
        self.mapping[key] = node

        if self.last is None:
            # First node
            self.first = self.last = node
        else:
            # Append at MRU
            node.prev = self.last
            self.last.next = node
            self.last = node

        # Evict LRU
        if len(self.mapping) > self.capacity:
            old = self.first

            self.first = old.next

            if self.first:
                self.first.prev = None
            else:
                # Cache became empty
                self.last = None

            del self.mapping[old.key]
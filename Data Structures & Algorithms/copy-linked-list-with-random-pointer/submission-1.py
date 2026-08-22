"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapping = {}

        curr = head
        while curr:
            mapping[curr] = Node(curr.val)
            curr = curr.next

        for original, copy in mapping.items():
            copy.next = mapping.get(original.next)
            copy.random = mapping.get(original.random)

        return mapping.get(head)
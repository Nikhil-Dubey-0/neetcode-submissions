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
        curr = head
        mapping = {}
        while curr:
            mapping[curr] = Node(curr.val,None,None)
            curr = curr.next
        for original, copy in mapping.items():
            copy.next = mapping.get(original.next,None)
            copy.random = mapping.get(original.random,None)
        for copies in mapping.values():
            return copies
            break
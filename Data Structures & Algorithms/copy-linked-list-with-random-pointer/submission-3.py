import collections
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
        copies = defaultdict(lambda: Node(0))  
        # this automatically create a key:value if it not exist yet
        copies[None] = None # handle if next or random is None

        curr = head
        while curr:
            copies[curr].val = curr.val
            copies[curr].next = copies[curr.next] 
        # defaultdict automatically create a pair if curr.next does not exist yet, cpoies[curr.next] = Node(0)
            copies[curr].random = copies[curr.random]
        # same here with copies[curr.random]
            curr = curr.next
        return copies[head]
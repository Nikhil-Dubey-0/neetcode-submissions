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
        # defaultdict automatically create a Node if it not exist yet
            copies[curr].val = curr.val
            copies[curr].next = copies[curr.next] 
            copies[curr].random = copies[curr.random]
            curr = curr.next
        return copies[head]
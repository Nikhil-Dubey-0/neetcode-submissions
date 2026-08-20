# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = {}
        curr = head
        while curr is not None:
            if curr is not None and visited.get(curr) == 1:
                return True
                break
            visited[curr] = 1
            curr = curr.next
        return False
        
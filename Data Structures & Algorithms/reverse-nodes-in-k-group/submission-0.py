# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr)
            curr = curr.next
        for i in range(0, len(values), k):
            # Only reverse if there are at least k elements left
            if i + k <= len(values):
                values[i : i + k] = values[i : i + k][::-1]
        dummy = ListNode(0)
        curr = dummy
        for node in values:
            curr.next = node
            curr = curr.next
        curr.next = None
        return dummy.next

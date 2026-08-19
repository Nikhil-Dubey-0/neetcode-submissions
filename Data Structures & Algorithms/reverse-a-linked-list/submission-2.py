# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        # 1 -> 2 -> 3 -> 4
        if head.next is None:
            return head  # at last, returns last node (4)
        
        newHead = self.reverseList(head.next)
         # from back (4 -> 3 -> 2 -> 1)
        head.next.next = head 
        head.next = None
        #  at 3 (3.next.next = 3), but 3.next is 4
        # so 3.next.next means 4.next which is set as 3
        # and 3.next is None

        # same, for 2, (2.next.next = 2), but 2.next is 3
        # so 2.next.next means 3.next which is set as 2
        # and 2.next is None

        # eventually it become 4 -> 3 -> 2 -> 1 -> None

        return newHead
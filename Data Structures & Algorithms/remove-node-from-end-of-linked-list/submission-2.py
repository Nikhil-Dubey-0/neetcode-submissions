class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        # Keep n nodes between left and right
        for _ in range(n):
            right = right.next

        # Move both until right reaches the end
        while right:
            left = left.next
            right = right.next

        # left is now the node before the one to remove
        left.next = left.next.next

        return dummy.next
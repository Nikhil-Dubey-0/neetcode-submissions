class Solution:
    def reverseKGroup(self, head, k):

        dummy = ListNode(0)
        dummy.next = head

        group_prev = dummy

        while True:

            # Find kth node
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            # Save node after this group
            group_next = kth.next

            # Save the first node.
            # After reversal, this becomes the LAST node.
            group_start = group_prev.next

            # Reverse group
            prev = group_next
            curr = group_start

            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # kth is now the first node
            group_prev.next = kth

            # group_start is now the last node.
            # It is immediately before the next group.
            group_prev = group_start
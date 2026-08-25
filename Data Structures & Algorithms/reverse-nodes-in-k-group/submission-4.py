class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        gp = dummy
        while True:
            kth = gp
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            gn = kth.next

            prev = gn
            curr = gp.next
            while curr != gn:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = gp.next
            gp.next = prev
            gp = temp
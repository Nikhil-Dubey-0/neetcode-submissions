# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        curr = prev
        x=1
        last = None
        while curr:
            if x == n:
                if last == None:
                    prev = curr.next
                    break
                if curr:
                    last.next = curr.next
                    break
                else:
                    last.next = None
                    break
            last = curr
            curr = curr.next
            x+=1
        
        prev, curr = None, prev
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

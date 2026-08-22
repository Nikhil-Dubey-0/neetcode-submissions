# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = ListNode(0,None)
        carry = 0
        while l1 or l2 or carry:
            v = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            dig = v % 10
            carry = v // 10

            new = ListNode(dig)
            prev.next = new
            prev = new
            l1,l2 = (l1.next if l1 else 0), (l2.next if l2 else 0)
        return head.next


            
            
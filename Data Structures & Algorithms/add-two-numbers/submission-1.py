# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = prev = ListNode(0,None)
        carry = 0
        while l1 and l2:
            v = l1.val + l2.val + carry
            dig = v%10
            carry = (v-dig)//10

            new = ListNode(dig)
            prev.next = new
            prev = new
            l1,l2 = l1.next, l2.next
        l = l1 or l2
        while l:
            v = carry + l.val
            dig = v%10
            carry = (v-dig)//10
            new = ListNode(dig)
            prev.next = new
            prev = new
            l = l.next
        while carry != 0:
            dig = carry % 10
            carry = (carry-dig) // 10
            new = ListNode(dig)
            prev.next = new
            prev = new
        return head.next


            
            
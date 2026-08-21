# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = {}
        curr = head
        i=0
        nodes[i] = curr
        while curr:
            curr = curr.next
            i+=1
            nodes[i] = curr
        i = i-1
        j=1
        x = 2
        while j <= i:
            if x%2==0:
                head.next = nodes[i]
                head = head.next
                i-=1
                x+=1
            else:
                head.next = nodes[j]
                head = head.next
                j+=1
                x+=1
        head.next = None
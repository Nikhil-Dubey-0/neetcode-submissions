# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            head = curr= list1
            curr1 = list1.next
            curr2 = list2
        else:
            head = curr = list2
            curr1 = list1
            curr2 = list2.next
        while curr1 is not None and curr2 is not None:
            if curr1.val <= curr2.val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next
            elif curr1.val > curr2.val:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next
        if curr1 is not None:
                curr.next = curr1
        if curr2 is not None:
                curr.next = curr2
        return head
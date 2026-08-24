# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        while len(lists)>1:
            nodes = []
            for i in range(len(lists)):
                if i%2 != 0:
                    dummy = ListNode(0)
                    curr = dummy
                    while lists[i-1] and lists[i]:
                        if lists[i-1].val <= lists[i].val:
                            curr.next = lists[i-1]
                            lists[i-1] = lists[i-1].next
                        else:
                            curr.next = lists[i]
                            lists[i] = lists[i].next
                        curr = curr.next
                    curr.next = lists[i-1] or lists[i]
                    nodes.append(dummy.next)
            if len(lists) % 2 != 0:
                nodes.append(lists[-1])
            lists = nodes
        if lists:
            return lists[0]
        return None
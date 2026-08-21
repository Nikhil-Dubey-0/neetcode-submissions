# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
# curr = head → both point to the same node
# curr.val = x → modifies the shared node, so head.val also changes
# curr.next = x → modifies the shared node, so head.next also changes

# curr = curr.next → only moves the curr reference
# head still points to the original node

# Arrays aren't special:
# nodes[0] and head can point to the same node
# nodes[0].val = x → head.val also changes
# nodes[0] = another_node → only changes the array element
"""
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        i, j = 0, len(nodes)-1
        # while i < j:
        #     head.next = nodes[j]
        #     head = head.next
        #     i += 1
        #     if i >= j:
        #         break
        #     head.next = nodes[i]
        #     head = head.next
        #     j -= 1
        # head.next = None
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break
            nodes[j].next = nodes[i]
            j -= 1
        nodes[i].next = None # so they both work



        
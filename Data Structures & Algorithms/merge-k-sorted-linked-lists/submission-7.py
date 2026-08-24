import heapq

# standard heap solution
class Solution:
    def mergeKLists(self, lists):
        heap = []

        # Put first node of every list into heap
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            # Smallest available node goes into result
            tail.next = node
            tail = node

            # Put the next node from the same list into heap
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
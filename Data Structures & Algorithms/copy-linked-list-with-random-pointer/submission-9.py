class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # 1. Interleave copied nodes
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        # 2. Set random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # Save copy head BEFORE separating
        copy_head = head.next

        # 3. Separate the two lists
        curr = head
        while curr:
            copy = curr.next

            curr.next = copy.next

            if copy.next:
                copy.next = copy.next.next

            curr = curr.next

        return copy_head
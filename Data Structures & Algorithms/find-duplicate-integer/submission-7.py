class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        # Treat the array as a linked list:
        #
        #     index i  →  nums[i]
        #
        # Example:
        # nums = [1, 3, 4, 2, 2]
        #
        # Because there is a duplicate, 
        # this "linked list" must contain a cycle.
        # The duplicate number is the START of the cycle.
        '''     
        # Why?
        # Every index has exactly ONE outgoing edge: i → nums[i].
        # Since nums contains n+1 values in [1, n], eventually we must
        # revisit a value. The first repeated value creates the cycle.
        #
        # The duplicate is exactly where two different nodes point
        # into the same node, so that node becomes the cycle entrance.
        '''
        # ---------------------------------------------------------
        # PHASE 1: Find a meeting point inside the cycle
        # ---------------------------------------------------------

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]              # move 1 step
            fast = nums[nums[fast]]        # move 2 steps

            if slow == fast:
                break

        # IMPORTANT:
        # slow == fast only tells us:
        #     "We are somewhere inside the cycle."
        #
        # It does NOT necessarily mean this node is the duplicate.

        # ---------------------------------------------------------
        # PHASE 2: Find the cycle entrance
        # ---------------------------------------------------------

        # Put slow back at the beginning.
        slow = nums[0]

        # Move both one step at a time.
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        # They meet at the cycle entrance.
        # The cycle entrance is the duplicate number.
        return slow

""" Why 2nd phase work?
Let,
a = distance from START → cycle entrance
b = distance from cycle entrance → first meeting point
C = cycle length

At the first meeting:
slow travelled = a + b

Fast travelled twice as far:
fast travelled = 2(a + b)

But fast may have gone around the cycle several extra times. So:
fast = a + b + kC
where k is some positive integer.

Therefore:
2(a + b) = a + b + kC

Simplify:
a + b = kC     =>    a = kC - b

And it can be rewritten as:
kC - b = (k - 1)C + (C - b)

So:
a = (k - 1)C + (C - b)

The important part is:

distance START → entrance
        =
distance MEETING → entrance + whole number of cycles

Therefore, when we do:

slow = START
fast = MEETING POINT

and move both one step at a time, they reach the cycle entrance simultaneously.

The extra (k - 1) complete cycles don't matter because fast just goes around the cycle and arrives at the same entrance.
"""
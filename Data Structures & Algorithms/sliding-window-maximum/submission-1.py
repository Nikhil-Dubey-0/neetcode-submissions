from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        dq = deque()      # Stores INDICES, not values
        res = []

        for right in range(len(nums)):

            # 1. Remove indices that are outside the current window
            while dq and dq[0] < right - k + 1:
                dq.popleft()

            # 2. Remove all smaller elements from the back
            # They can never become the maximum again
            while dq and nums[dq[-1]] < nums[right]:
                dq.pop()

            # 3. Add current index
            dq.append(right)

            # 4. First complete window formed
            if right >= k - 1:
                res.append(nums[dq[0]])

        return res
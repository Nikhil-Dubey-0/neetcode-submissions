class Solution:
    def firstMissingPositive(self, nums):
        
        nums = [int(x) for x in nums if x > 0]

        n = len(nums)

        i = 0
        while i < n:
            correct = nums[i] - 1 # The correct index where nums[i] should be placed.

            if (
                1 <= nums[i] <= n  # n between (1 and n), Ignore negatives, 0, and numbers greater than n.
                and nums[i] != nums[correct]  # The correct position doesn't already contain the same number (infinite handling)
            ):
                nums[i], nums[correct] = nums[correct], nums[i]   #  Put the current number into its correct position. (swap)
                # DO NOT increase i here. (After swapping, That new number may also need to be moved.)
            else:
                i += 1  # Nothing more can be done for this index.

        for i in range(n):
            if nums[i] != i + 1:
                return i+1
                break
        else:
            return n+1
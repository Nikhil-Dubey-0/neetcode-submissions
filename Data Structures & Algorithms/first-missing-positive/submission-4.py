class Solution:
    def firstMissingPositive(self, nums):
        
        nums = [int(x) for x in nums if x > 0]

        n = len(nums)

        i = 0
        while i < n:
            correct = nums[i] - 1

            if (
                1 <= nums[i] <= n
                and nums[i] != nums[correct]
            ):
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i+1
                break
        else:
            return n+1
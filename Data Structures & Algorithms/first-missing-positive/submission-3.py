class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)

        seen = [False] * (n + 1)

        for x in nums:
            if 1 <= x <= n:
                seen[x] = True

        for i in range(1, n + 1):
            if not seen[i]:
                return i

        return n + 1
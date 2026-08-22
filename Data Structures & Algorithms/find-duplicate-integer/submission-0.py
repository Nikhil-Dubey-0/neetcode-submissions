class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums = sorted(nums)
        prev = None
        for i in nums:
            if i == prev:
                return prev
            prev = i
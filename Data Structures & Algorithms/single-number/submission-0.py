from collections import Counter
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        coun = Counter(nums)
        for k, v in coun.items():
            if v == 1:
                return k
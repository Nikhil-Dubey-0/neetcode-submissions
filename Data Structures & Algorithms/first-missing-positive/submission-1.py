class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        integer = set()

        for x in nums:
            if x>0 and x.is_integer():
                integer.add(x)
        ans = 1
        while ans in integer:
            ans+=1
        return ans
            
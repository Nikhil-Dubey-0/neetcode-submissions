class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        s=set(nums)
        for num in range(1,len(s)+1):
            if num not in s:
                return num
            
        return max(nums)+1
            
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        length=len(nums)
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            if freq[num]>length//2:
                return num
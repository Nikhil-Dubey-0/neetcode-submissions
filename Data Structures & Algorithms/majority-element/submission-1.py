class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq={}
        length=len(nums)
        for num in nums:
            if num in freq:
                freq[num]+=1
            else:
                freq[num]=1
            if freq[num]>length/2:
                return num
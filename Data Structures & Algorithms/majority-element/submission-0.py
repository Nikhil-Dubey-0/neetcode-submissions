class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        length=len(nums)
        num_set=set(nums)
        for num in num_set:
            if nums.count(num)>length/2:
                return num
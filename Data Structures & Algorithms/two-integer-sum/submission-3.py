class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dic={}
        for i,num in enumerate(nums):
            diff = target-num
            if diff in my_dic:
                return [my_dic[diff],i]
            my_dic[num]=i
        return
            
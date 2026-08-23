class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            index = abs(num) - 1
            # if a number is 3, 
            # i make whatever num in index 2 as negative 
            # then check for new num on same index
            if nums[index] < 0:
                return abs(num)  
                # there is  a  chance that the number was already set negative by some prev number, so use abs(num)
            nums[index] *= -1
        
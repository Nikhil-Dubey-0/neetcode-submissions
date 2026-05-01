class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        for i in nums:
            mul*=i

        count=nums.count(0)
        my_list=[]
        
        if count==1:
            mul1=1
            for i in nums:
                if i!=0:
                    mul1*=i
            for i in nums:
                if i==0:
                    my_list.append(int(mul1))
                else:
                    my_list.append(0)
        elif count>=2:
            return [0] * len(nums)
        else:
            for num in nums:

                my_list.append(mul//num)
        

        return my_list

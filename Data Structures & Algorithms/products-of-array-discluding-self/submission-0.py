class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mul=1
        for i in nums:
            mul*=i

        count=nums.count(0)
        my_list=[]
        
        for i in nums:
            if count==1:
                mul1=1
                for j in nums:
                    if j!=0:
                        mul1*=j
                if i==0:
                    my_list.append(int(mul1))
                else:
                    my_list.append(0)
            elif count>=2:
                return [0] * len(nums)
            else:
                my_list.append(mul//i)
        

        return my_list

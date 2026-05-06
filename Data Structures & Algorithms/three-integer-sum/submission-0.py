class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res=set()

        
        for k in range(len(s_nums)-2):
            i,j=k+1,len(s_nums)-1
            while  i<j:
                if s_nums[i]+s_nums[j]+s_nums[k]==0:
                    res.add((s_nums[k], s_nums[i], s_nums[j]))
                    i+=1
                    j-=1
                elif s_nums[i]+s_nums[j]+s_nums[k]>0:
                    j-=1
                else:
                    i+=1
    
        result = [list(t) for t in res]

        return result
            
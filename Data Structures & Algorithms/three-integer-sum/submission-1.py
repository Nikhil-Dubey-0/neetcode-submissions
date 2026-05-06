class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        res=[]

        
        for k in range(len(s_nums)-2):
            if s_nums[k] > 0:  # optimization
                break

            if k!=0 and s_nums[k]==s_nums[k-1]:
                continue

            i,j=k+1,len(s_nums)-1
            while  i<j:
                sum = s_nums[k] + s_nums[i] + s_nums[j]
                if sum==0:
                    res.append([s_nums[k], s_nums[i], s_nums[j]])
                    i+=1
                    j-=1

                    # skip duplicate i values
                    while i < j and s_nums[i] == s_nums[i - 1]:
                        i += 1

                    # skip duplicate j values
                    while i < j and s_nums[j] == s_nums[j + 1]:
                        j -= 1

                elif sum>0:
                    j-=1
                else:
                    i+=1
    

        return res
            
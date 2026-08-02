class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res=[]
        counter = [0]*100001
        for num in nums:
            counter[num+50000]+=1
        for i,val in enumerate(counter):
            while val!=0:
                res.append(i-50000)
                val-=1
        return res
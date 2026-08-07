class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length=len(nums)
        maxi=max(max(nums),length)
        arr = [0]*maxi

        for i in nums:
            if i>0:
                arr[i-1]=1
        for i in range(maxi):
            if arr[i]==0:
                return i+1
        return length+1


        
            
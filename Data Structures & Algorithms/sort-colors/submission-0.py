class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counter = [0]*3
        for num in nums:
            counter[num]+=1
        x=0
        for color,count in enumerate(counter):
            for _ in range(count):
                nums[x]=color
                x+=1
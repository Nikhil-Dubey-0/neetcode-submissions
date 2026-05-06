class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)<2:
            return 0
        i,j=0,len(height)-1
        
        area=0
        while i<j:
            if height[i]>height[j]:
                if height[j-1]>=height[j]:
                    j-=1
                else:
                    diff =height[j]
                    while height[j-1]<diff and i<j:
                        area+=diff-height[j-1]
                        j-=1
            else:
                if height[i+1]>=height[i]:
                    i+=1
                else:
                    diff = height[i]
                    while height[i+1]<diff and i<j:
                        area+=diff-height[i+1]
                        i+=1

        return area
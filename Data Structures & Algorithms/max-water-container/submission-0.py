class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights)<2:
            return 0
        i,j=0,len(heights)-1
        area=0
        
        while i<j:
            curr_area = min(heights[i],heights[j]) * (j-i)
            area=max(curr_area,area)

            if heights[i]>heights[j]:
                j-=1
            elif heights[i]<heights[j]:
                i+=1
            else:
                if heights[i+1]>heights[j-1]:
                    i+=1
                elif heights[i+1]<heights[j-1]:
                    j-=1
                else:
                    i+=1
                    j-=1

        return area
            
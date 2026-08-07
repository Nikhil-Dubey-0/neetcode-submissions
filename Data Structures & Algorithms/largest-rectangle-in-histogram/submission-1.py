class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area=0
        left = [0]*len(heights)
        for index, height in enumerate(heights):
            start = index
            while stack and height<heights[stack[-1]]:
                val = stack.pop()
                area = max(area,(index-left[val])*heights[val])
                start = left[val]
            left[index] = start
            stack.append(index)
        while stack:
            val = stack.pop()
            area = max(area,(len(heights)-left[val])*heights[val])
        return area

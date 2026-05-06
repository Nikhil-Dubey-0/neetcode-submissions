class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max = right_max = area = 0
    
        while i < j:
            if height[i] <= height[j]:
                left_max = max(left_max, height[i])
                area += left_max - height[i]
                i += 1
            else:
                right_max = max(right_max, height[j])
                area += right_max - height[j]
                j -= 1
    
        return area
class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        left_max = height[i]
        right_max = height[j]
        area = 0

        while i < j:
            if left_max < right_max:
                i += 1
                left_max = max(left_max, height[i])
                area += left_max - height[i]
            else:
                j -= 1
                right_max = max(right_max, height[j])
                area += right_max - height[j]

        return area
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        left = 0
        right = (rows*cols)-1
        while left <= right:
            mid = (right+left) // 2
            if matrix[mid//cols][mid%cols] ==target:
                return True
            elif matrix[mid//cols][mid%cols] < target:
                    left = mid+1
            else:
                right = mid-1
        return False
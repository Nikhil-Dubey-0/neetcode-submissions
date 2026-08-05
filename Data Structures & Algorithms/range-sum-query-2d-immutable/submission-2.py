class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.Matrix = matrix
        for i,row in enumerate(self.Matrix):
            row_sum=0
            for j,col_val in enumerate(row):
                row_sum += col_val
                if i-1>-1:
                    self.Matrix[i][j] = row_sum+self.Matrix[i-1][j]  
                else:
                    self.Matrix[i][j] = row_sum


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 > 0 and col1 > 0:
            return self.Matrix[row2][col2] + self.Matrix[row1-1][col1-1] - self.Matrix[row1-1][col2] - self.Matrix[row2][col1-1]
        elif row1 == 0 and col1 > 0:
            return self.Matrix[row2][col2] - self.Matrix[row2][col1-1]
        elif row1 > 0 and col1 == 0:
            return self.Matrix[row2][col2] - self.Matrix[row1-1][col2]
        else:
            return self.Matrix[row2][col2]
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
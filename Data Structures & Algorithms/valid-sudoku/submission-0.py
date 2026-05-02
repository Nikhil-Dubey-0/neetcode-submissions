class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h_row={}
        h_col={}
        h_box={}



        for i,rows in enumerate(board):
            for j in range(9):
                if j not in h_col:
                    h_col[j]=set()
                if rows[j]!=".":
                    if rows[j] in h_col[j]:
                        return False
                    h_col[j].add(rows[j])
        

                if i not in h_row:
                    h_row[i]=set()
                if rows[j]!=".":
                    if rows[j] in h_row[i]:
                        return False
                    h_row[i].add(rows[j])


            # box[x][y] = board[i//3][j//3]

                x=i//3
                y=j//3
                if (x,y) not in h_box:
                    h_box[(x,y)]=set()
                if rows[j]!=".":
                    if rows[j] in h_box[(x,y)]:
                        return False
                    h_box[(x,y)].add(rows[j])




    



        return True

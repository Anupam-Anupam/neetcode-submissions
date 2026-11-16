class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        matrix = [["."] * n for _ in range(n)]
        matrices  = []
        cols = set()
        pdiagonals = set()
        ndiagonals = set()
        

        def issafe(row, col):

            if col not in cols and (row-col) not in ndiagonals and (row+col) not in pdiagonals:
                return True

        
        def backtrack(row):
 
            if row == n:
                matrices.append(["".join(x) for x in matrix])
                return


            for col in range(n):

                if not issafe(row, col):
                    continue


                matrix[row][col] = "Q"
                cols.add(col)
                ndiagonals.add(row - col)
                pdiagonals.add(row + col)

                backtrack(row+1)

                matrix[row][col] = "."
                cols.remove(col)
                ndiagonals.remove(row - col)
                pdiagonals.remove(row + col)
            
                    
        
        
        backtrack(0)
        
        return matrices
        








    
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for rows in range(9):
            seen1 = set()
            for col in range(9):
                if board[rows][col] == ".":
                    continue  
                if board[rows][col] in seen1:
                    return False
                else: 
                    seen1.add(board[rows][col])

        for rows in range(9):
            seen2 = set()
            for col in range(9):
                if board[col][rows] == ".":
                    continue 
                if board[col][rows] in seen2:
                    return False
                else: 
                    seen2.add(board[col][rows])
        
        for square in range(9):
            seen3 = set()
            for i in range(3):
                for j in range(3):
                    row = (square//3)*3 + i
                    col = (square%3)*3 + j
                    if board[row][col] == ".":
                        continue
                    if board[row][col] in seen3:
                        return False
                    else: 
                        seen3.add(board[row][col])
                    
        return True
                
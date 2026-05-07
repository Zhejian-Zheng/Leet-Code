class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # 1. Check all rows
        for i in range(9):
            valid = [False] * 9  # Reset for each row
            for j in range(9):
                if board[i][j] == '.': 
                    continue
                t = int(board[i][j]) - 1  # Convert to int to use as an index
                if valid[t]: 
                    return False
                valid[t] = True

        # 2. Check all columns
        for i in range(9):
            valid = [False] * 9  # Reset for each column
            for j in range(9):
                if board[j][i] == '.': 
                    continue
                t = int(board[j][i]) - 1
                if valid[t]: 
                    return False
                valid[t] = True

        # 3. Check all 3x3 sub-boxes
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                valid = [False] * 9  # Reset for each 3x3 sub-box
                
                # Iterate through the 3x3 grid
                for x in range(3):
                    for y in range(3):
                        if board[i + x][j + y] == '.': 
                            continue
                        t = int(board[i + x][j + y]) - 1
                        if valid[t]: 
                            return False
                        valid[t] = True

        return True
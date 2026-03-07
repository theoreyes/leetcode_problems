# Author: Theodore Reyes
# Explanation: O(n) solution to the Valid Sudoku problem.
# Involves one pass-through of the board, where we keep
# track of numbers using sets for each row, column, and
# 3x3 sub-grid.
#
# Note: If we let n be the length of one side of the board,
# we get the following time and space complexities:
#   
# Time: O(n^2)
# Space: O(n^2)      

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        cols = list()
        rows = list()
        grids = list()

        # Create sets for holding sudoku cols/rows/grids
        for i in range(9):
            cols.insert(i, set())
            rows.insert(i, set())
            grids.insert(i, set())
        
        for j in range(9):
            for i in range(9):
                
                # Ignores empty cells
                if (board[i][j] == "."): continue

                # Check/add to cols
                if board[i][j] in cols[i]: return False
                cols[i].add(board[i][j])
                
                # Add to row
                if board[i][j] in rows[j]: return False
                rows[j].add(board[i][j])

                # Add to grids
                if board[i][j] in grids[(i // 3) + (3 * (j // 3))]: return False
                grids[(i // 3) + (3 * (j // 3))].add(board[i][j])

        # If loop completed, board is valid
        return True;


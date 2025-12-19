# Theo Reyes
#
# Explanation: Naive-approach solution to Valid Sudoku problem.
# Simply checks each row, col, and 3x3 subgrid for invalid
# patterns, and returns True at the end if none found.
# Time: O(n^2)
# Space: O(n)

class Solution(object):
    def isValidSudoku(self, board):
        numSeen = set()
        
        # Check rows
        for row in board:
            numSeen.clear()
            for item in row:
                if item == ".":
                    continue
                else:
                    if item in numSeen: 
                        return False
                    else: 
                        numSeen.add(item)

        # Check columns
        for i in range(len(board)):
            numSeen.clear()
            for j in range(len(board)):
                if board[j][i] == ".":
                    continue
                else:
                    if board[j][i] in numSeen:
                        return False
                    else:
                        numSeen.add(board[j][i])

        # Check 3x3 sub-grids
        for igrid in range(3):
            for jgrid in range(3):
                numSeen.clear()
                for i in range(igrid*3, igrid*3 + 3):
                    for j in range(jgrid*3, jgrid*3 + 3):
                        if board[i][j] == ".":
                            continue
                        else:
                            if board[i][j] in numSeen:
                                return False
                            else:
                                numSeen.add(board[i][j])
        return True

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(set)
        column = defaultdict(set)
        grid = defaultdict(list)
        board_len = len(board)
        for r in range(board_len):
            for c in range(board_len):
                if(board[r][c] in row[r] or board[r][c] in column[c] or board[r][c] in grid[(r//3,c//3)]):
                    return False
                if(board[r][c]!='.'):
                    row[r].append(board[r][c])
                    column[c].append(board[r][c])
                    grid[(r//3,c//3)].append(board[r][c])
                    print(grid)
        return True

sol = Solution()
ans = sol.isValidSudoku([[".","8","7","6","5","4","3","2","1"],
["2",".",".",".",".",".",".",".","."],
["3",".",".",".",".",".",".",".","."],
["4",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".",".","."],
["6",".",".",".",".",".",".",".","."],
["7",".",".",".",".",".",".",".","."],
["8",".",".",".",".",".",".",".","."],
["9",".",".",".",".",".",".",".","."]])

print(ans)
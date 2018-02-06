import math
class Solution:
    # @param {character[][]} board
    # @return {boolean}
    def isValidSudoku(self, board):
        if not board:
            return False

        row, col, box = [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    index = int(num) - 1
                    print(i,j)
                    k = ((i // 3 * 3) + (j // 3))
                    if row[i][index] or col[j][index] or box[k][index]:
                        return False

                    row[i][index] = col[j][index] = box[k][index] = True

        return True

var=Solution()
print(var.isValidSudoku([
                   [".","8","7","6","5","4","3","2","1"],
                   ["2",".",".",".",".",".",".",".","."],
                   ["3",".",".",".",".",".",".",".","."],
                   ["4",".",".",".",".",".",".",".","."],
                   ["5",".",".",".",".",".",".",".","."],
                   ["6",".",".",".",".",".",".",".","."],
                   ["7",".",".",".",".",".",".",".","."],
                   ["8",".",".",".",".",".",".",".","."],
                   ["9",".",".",".",".",".",".",".","."]
]))
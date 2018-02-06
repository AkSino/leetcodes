class Solution:
    def updateBoard(self, board, click):

        x, y = click[0], click[1]
        if board[x][y] == 'M':
            board[x][y] = 'X'
        else:
            self.reveal(board, x, y)
        return board

    def ismine(self, board, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return False
        if board[x][y] == 'M':
            return True

    def reveal(self, board, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] != 'E':
            return

        neighbours = [
            (x + 1, y),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x, y + 1),
            (x, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
            (x - 1, y - 1)]
        minecount = 0
        for a, b in neighbours:
            if self.ismine(board, a, b):
                minecount += 1

        if minecount == 0:
            board[x][y] = 'B'
            for a, b in neighbours:
                self.reveal(board, a, b)
        else:
            board[x][y] = str(minecount)

var=Solution()
print(var.updateBoard([['E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'M', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'E'],
                       ['E', 'E', 'E', 'E', 'E']],
                       [3,0]))
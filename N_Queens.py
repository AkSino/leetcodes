class Solution:
    def solveNQueens(self, n):
        array=[[i for i in range(4)] for i in range(n)]
        print(array[1][2])

    def helperFunction(self, array, row):
        for i in range(len(array)):
            if(self.checkForCorrectness(array, row, i)):
                array[row][i] = 1
                self.helperFunction(array, row+1)
                array[row][i] = 0

    def checkForCorrectness(self, array, row, column):



var=Solution()
var.solveNQueens(4)
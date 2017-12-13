class Solution:
    def __init__(self):
        self.visited=[]
    def dfs(self,i, j, matrix,xx,yy):
        x = [0, 0, 1, -1]
        y = [1, -1, 0, 0]
        for m in range(len(x)):
            if (0 <= i + x[m] < xx and 0 <= y[m] + j < yy and self.visited[i + x[m]][y[m] + j] == False and matrix[i + x[m]][y[m] + j] == "1"):
                self.visited[i + x[m]][y[m] + j] = True
                self.dfs(i + x[m], j + y[m], matrix,xx,yy)

    def numIslands(self, matrix):
        self.visited  = [[False for i in range(len(matrix[0]))] for j in range(len(matrix))]
        xx=len(matrix)
        if matrix[0]:
            yy=len(matrix[0])
        else:
            yy =0
        p=matrix
        count = 0
        for i in range(xx):
            for j in range(yy):
                if ((p[i][j] == "1") and (self.visited[i][j] == False)):
                    self.visited[i][j] = True
                    self.dfs(i, j, p,xx,yy)
                    count += 1
        return count
matrix=[["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
vardan=Solution()
print(vardan.numIslands(matrix))



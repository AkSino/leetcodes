import sys
class Solution:
    def minPathSum(self, grid):
        if len(grid)==0:
            return 0
        trace_matrix=[[0 for i in range(len(grid[0])+1)] for j in range(len(grid)+1)]
        trace_matrix[1][1]=grid[0][0]
        for i in range(1,len(trace_matrix)):
            for j in range(1,len(trace_matrix[0])):
                if i==1:
                    trace_matrix[i][j]=grid[i-1][j-1]+trace_matrix[i][j-1]
                    continue
                if j==1:
                    trace_matrix[i][j] = grid[i - 1][j - 1] + trace_matrix[i-1][j]
                    continue
                trace_matrix[i][j]=min(grid[i-1][j-1]+trace_matrix[i-1][j],grid[i-1][j-1]+trace_matrix[i][j-1])
        return trace_matrix[len(grid)][len(grid[0])]

var=Solution()
print(var.minPathSum([[1,3,1],
 [1,5,1],
 [4,2,1]]))




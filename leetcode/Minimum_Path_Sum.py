#https://leetcode.com/problems/minimum-path-sum/description/
import sys
class Solution:
    def support(self, m, n, grid,trace):
        x=[1,0]
        y=[0,1]
        ans=0

        if m>len(grid)-1 or n>len(grid[0])-1:
            return sys.maxsize
        if trace[m][n]:
            return trace[m][n]
        if m==len(grid)-1 and n==len(grid[0])-1:
            return grid[m][n]
        ans=min(grid[m][n] + self.support(m+x[0],n+y[0],grid,trace),grid[m][n] + self.support(m+x[1],n+y[1],grid,trace))
        trace[m][n]=ans
        return ans
    def minPathSum(self, grid):
        trace=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
        p=self.support(0,0,grid,trace)
        if len(grid)==0:
            return 0
        return p

var=Solution()
print(var.minPathSum([[7,1,3,5,8,9,9,2,1,9,0,8,3,1,6,6,9,5],[9,5,9,4,0,4,8,8,9,5,7,3,6,6,6,9,1,6],[8,2,9,1,3,1,9,7,2,5,3,1,2,4,8,2,8,8],[6,7,9,8,4,8,3,0,4,0,9,6,6,0,0,5,1,4],[7,1,3,1,8,8,3,1,2,1,5,0,2,1,9,1,1,4],[9,5,4,3,5,6,1,3,6,4,9,7,0,8,0,3,9,9],[1,4,2,5,8,7,7,0,0,7,1,2,1,2,7,7,7,4],[3,9,7,9,5,8,9,5,6,9,8,8,0,1,4,2,8,2],[1,5,2,2,2,5,6,3,9,3,1,7,9,6,8,6,8,3],[5,7,8,3,8,8,3,9,9,8,1,9,2,5,4,7,7,7],[2,3,2,4,8,5,1,7,2,9,5,2,4,2,9,2,8,7],[0,1,6,1,1,0,0,6,5,4,3,4,3,7,9,6,1,9]]))



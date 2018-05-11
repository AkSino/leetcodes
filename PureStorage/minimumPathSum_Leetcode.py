# class Solution:
#     def minPathSum(self, grid):
#         if len(grid)==0:
#             return 0
#         return self.helper(grid[0][0],0,0,grid)
#     def helper(self,sum,xaxis,yaxis,grid):
#         if xaxis==len(grid)-1 and yaxis==len(grid[0])-1:
#             return sum
#         x=[1,0]
#         y=[0,1]
#         mini=1000000000000
#         for i in range(len(x)):
#             if xaxis+x[i]<len(grid) and yaxis+y[i]<len(grid[0]):
#                 mini=min(mini,self.helper(sum+grid[xaxis+x[i]][yaxis+y[i]],xaxis+x[i],yaxis+y[i],grid))
#         return mini

class Solution:
    def minPathSum(self, grid):
        grid2=[[10000000 for d in range(len(grid[0]))] for c in range(len(grid))]
        x=[-1,0]
        y=[0,-1]
        grid2[0][0]=grid[0][0]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                for m in range(len(x)):
                    if i+x[m]>=0 and j+y[m]>=0:
                        grid2[i][j]=min(grid2[i][j],grid[i][j]+grid2[i+x[m]][j+y[m]])
        return grid2[len(grid)-1][len(grid[0])-1]

vatr=Solution()
print(vatr.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
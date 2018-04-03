#https://leetcode.com/problems/cherry-pickup/description/
from copy import deepcopy

class Solution:
    def cherryPickup(self, grid):
        return self.helper(grid,0,0)

    def helper(self,grid,start,end):
        x=[0,1]
        y=[1,0]
        maxi=0
        array_ret = deepcopy(grid)
        if start==len(grid)-1 and end==len(grid[0])-1:
            if grid[start][end]>0:
                grid[start][end]-=1
                return [1,grid]
            else:
                return [0,grid]
        for i in range(len(x)):
            if (start+x[i]<len(grid) and end+y[i]<len(grid[0]) and grid[start+x[i]][end+y[i]]!=-1):


                if grid[start][end]>0:
                    grid[start][end]-=1
                    p = self.helper(grid, start + x[i], end + y[i])
                    if maxi<1+p[0]:
                        maxi=1+p[0]
                        c=p[1]
                        array_ret = deepcopy(c)
                    grid[start][end]+=1
                    t=1
                else:
                    p = self.helper(grid, start + x[i], end + y[i])
                    if maxi<p[0]:
                        maxi=p[0]
                        array_ret=p[1]

        return [maxi,array_ret]

grid =[ [0, -1, -1],
        [-1, -1, -1],
        [1, 1,  1]]
var=Solution()
print(var.cherryPickup(grid))
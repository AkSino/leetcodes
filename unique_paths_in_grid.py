def helper(grid,visited,i,j):
    if (i==len(grid)-1) and j==(len(grid[0])-1):
        return 1
    x=[0,1]
    y=[1,0]
    count=0
    for each in range(len(x)):
        if 0<=i+x[each]<len(grid) and 0<=j+y[each]<len(grid[0]) and grid[i+x[each]][j+y[each]]!=1 and visited[i+x[each]][j+y[each]]!=True:
            visited[i+x[each]][j+y[each]]=True
            count+=helper(grid,visited,i+x[each],j+y[each])
            visited[i+x[each]][j+y[each]] = False
    return count

def findUniquePath(grid):
    visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
    return helper(grid,visited,0,0)
a=[
  [0,1,0],
  [1,0,0],
  [0,0,0]
]
print(findUniquePath(a))


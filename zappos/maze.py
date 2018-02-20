final_ans=[]

def helper(grid,visited,i,j,printing_array):
    global final_ans
    if grid[i][j]==9:
        x=list(printing_array)
        final_ans+=[x]
    x=[0,1,-1,0]
    y=[1,0,0,-1]
    dict={0:"R",1:"D",2:"U",3:"L"}
    count=0
    another=printing_array
    for each in range(len(x)):
        if 0<=i+x[each]<len(grid) and 0<=j+y[each]<len(grid[0]) and grid[i+x[each]][j+y[each]]!=1 and visited[i+x[each]][j+y[each]]!=True:
            visited[i+x[each]][j+y[each]]=True
            another.append(dict[each])
            helper(grid,visited,i+x[each],j+y[each],another)
            another.pop()
            visited[i+x[each]][j+y[each]] = False
def findUniquePath(grid,start):

    startx=start[0]
    starty=start[1]
    visited=[[False for i in range(len(grid[0]))] for j in range(len(grid))]
    visited[startx][starty]=True
    return helper(grid,visited,startx,starty,[])
a=[
  [0,0,0],
  [0,0,0],
  [0,9,0]
]
i=0
j=1
(findUniquePath(a,[i,j]))
print(sorted(final_ans)[0])


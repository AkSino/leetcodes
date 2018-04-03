a=[[1,1,1,1,1,1],
   [1,1,1,1,1,1],
   [1,1,1,1,1,1]]


def cherryPickup(grid):
    return helper(grid, 0, 0,[],[])


def helper(grid, start, end, array,store):
    x = [0, 1]
    y = [1, 0]
    if start == len(grid) - 1 and end == len(grid[0]) - 1:
        array.append(store)
    else:
        for i in range(len(x)):
            if (start+x[i]<len(grid) and end+y[i]<len(grid[0])):
                helper(grid,start+x[i],end+y[i],array,store+[x[i]])

    return array

print(len(cherryPickup(a)))
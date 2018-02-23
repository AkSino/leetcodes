def function(puzzle_array):
    mines=[]
    x=[1,-1,0,0,-1,-1,1,1]
    y=[0,0,1,-1,-1,1,1,-1]
    result_array=[[0 for i in range(len(puzzle_array))] for j in range(len(puzzle_array))]
    for i in range(len(puzzle_array)):
        for j in range(len(puzzle_array[0])):
            if puzzle_array[i][j]== "m":
                mines.append([i,j])
                for p in range(len(x)):
                    if 0<=i+x[p]<len(puzzle_array) and 0<=j+y[p]<len(puzzle_array):
                        result_array[i+x[p]][j+y[p]]+=1
    for each in mines:
        x=each[0]+1
        if x<len(puzzle_array):
            result_array[x][each[1]] = 2
    for each in mines:
        y = each[1] + 1
        if y < len(puzzle_array):
            result_array[each[0]][y] = 0
    for i in range(1, len(puzzle_array), 2):
        if i in [elem[0] for elem in mines]:
            for j in range(len(puzzle_array)):
                result_array[i][j]*=3
    x = [-1, -1, 1, 1]
    y = [-1, 1, 1, -1]
    for i in range(len(puzzle_array)):
        for j in range(len(puzzle_array[0])):
            if puzzle_array[i][j]!= "m":
                for p in range(len(x)):
                    if 0<=i+x[p]<len(puzzle_array) and 0<=j+y[p]<len(puzzle_array) and puzzle_array[i + x[p]][j + y[p]]== 'm':
                        result_array[i][j]*=2
                        break
    for each in mines:
        result_array[each[0]][each[1]]=-1

    return result_array

for each in (function([
['.','m','.','.'],
['.','.','.','.'],
['.','.','.','m'],
['m','.','.','.']])):
    print(each)




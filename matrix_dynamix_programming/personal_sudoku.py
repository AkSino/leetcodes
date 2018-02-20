def find_in_rows(matrix,element,x,y):
    for i in range(0,9):
        if matrix[x][i]==element:
            if i!=y:
                return False
    return True

def find_in_cols(matrix,element,x,y):
    for i in range(0,9):
        if matrix[i][y]==element:
            if i!=x:
                return False
    return True

def find_in_box(matrix,element,x,y):
    array=[]
    for i in range(3):
        for j in range(3):
            if matrix[x // 3 + i][x // 3 + j] not in array:
                array.append(matrix[x//3+i][x//3+j])
            elif matrix[x // 3 + i][x // 3 + j]=="*":
                continue
            else:
                return False
    return True

def main_function(matrix):
    for i in range(9):
        for j in range(9):
            if matrix[i][j]=="*":
                for element in range(1,10):
                    matrix[i][j]=element
                    if i<9:
                        if  (find_in_rows(matrix,element,i,j) and find_in_cols(matrix,element,i,j) and find_in_box(matrix,element,i,j) and main_function(matrix)):
                            return True
                        else:
                            if element==9:
                                return False
                            continue
                    elif j<9:
                        if  (find_in_rows(matrix,element,i,j) and find_in_cols(matrix,element,i,j) and find_in_box(matrix,element,i,j) and main_function(matrix)):
                            return True
                        else:
                            if element==9:
                                return False
                            continue
                    else:
                        return True



a=[[0 for x in range(10)] for x in range(10)]
matrix=[["*" for x in range(9)] for u in range(9)]
(main_function(matrix,0,0))
print(matrix)




def helper(array,matrix,i):
    if i==len(array):
        print(matrix)
    else:
        matrix[i]=None
        helper(array,matrix,i+1)
        matrix[i]=array[i]
        helper(array,matrix,i+1)



def prints(array):
    matrix=[None for i in range(len(array))]
    helper(array,matrix,0)

prints([1,2])


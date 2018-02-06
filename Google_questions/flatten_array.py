def flattenArray(array):
    for each in array:
        if type(each)==int:
            print(each,end=" ")
        else:
            flattenArray(each)



flattenArray([1,2,[[3],4,5]])
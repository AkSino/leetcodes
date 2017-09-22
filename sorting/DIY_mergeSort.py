def mergeTwoArray(array1,array2):
    c=[]
    while len(array1)!=0 and len(array2)!=0:
        if array1[0]>array2[0]:
            c.append(array2[0])
            array2.remove(array2[0])
        else:
            c.append(array1[0])
            array1.remove(array1[0])
    if len(array1)==0:
        c=c+array2
    else:
        c=c+array1
    return c


def mergeSort(arra):
    if len(arra)==0 or len(arra)==1:
        return arra
    else:
        mid=int(len(arra)/2)
        left_half=mergeSort(arra[:mid])
        right_half=mergeSort(arra[mid:])
        return mergeTwoArray(left_half,right_half)



arra=[5,6,7,7,8]
print (mergeSort(arra))
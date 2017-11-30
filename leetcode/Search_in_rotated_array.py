#

array=[9,1,3,4,5,6,7,8]
def find_pivot(array,low,high):
    mid=int((low+high)/2)
    if array[mid]>array[mid+1]:
        return mid
    else:
        if array[mid]>array[low]:
            return find_pivot(array,mid+1,high)
        else:
            return find_pivot(array,low,mid-1)

def binary_search(arr,key,low,high):
    mid=int((low+high)/2)
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return binary_search(arr,key,mid+1,high)
    if key<arr[mid]:
        return binary_search(arr,key,low,mid-1)

def find_number(array,number,low,high):
    if array[low]<array[high]:
        print(binary_search(array,low,high))
    else:
        pivot=find_pivot(array,low,high)
        if number>=array[low]:
            print(binary_search(array,number,low,pivot))
        else:
            print(binary_search(array,number,pivot+1,high))



print(find_number(array,3,0,6))
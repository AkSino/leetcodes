#https://leetcode.com/problems/search-in-rotated-sorted-array/description/

input_array=[4,5,6,7,0,1,2]
low=0
high=len(input_array)-1

def FindPivot(input_array,low,high):
    mid=int((low+high)/2)
    if input_array[low]<input_array[high]:
        print("Array is sorted")
        #string is sorted
    if input_array[mid]>input_array[mid+1]:
        print(mid)
        return mid
    if input_array[mid]>input_array[low]:
        FindPivot(input_array,mid+1,high)
    else:
            FindPivot(input_array,a ja  ,mid-1)

FindPivot(input_array,0,6)

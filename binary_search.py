def BinarySearch(arr,key):
    mid=int(len(arr)/2)
    if key==arr[mid]:
        return mid
    if key>arr[mid]:
        return BinarySearch(arr[mid+1:len(arr)],key)
    if key<arr[mid]:
        return BinarySearch(arr[0:mid],key)

print(BinarySearch([1,2,3,4,5,6,7,8,9,10,11,12,13,15,16,23,34,45,56,67,78,89],2))


#NOTE: We are using array slicing which works as follows:
#If a=[1,2,3,4,5,6,7,8]
#then a[2:5]=[3,4,5]

#Algo works as follows:
#Firstly algo will find the mid term of given array, if element is found there it will return index. If element is greater than
#the mid element algo will recursively call the method again passing the sliced array of all elements greater than the mid term
#and vice versa

#Binary search(long_array)=Binary_search(shorter_array)=result of shorter array
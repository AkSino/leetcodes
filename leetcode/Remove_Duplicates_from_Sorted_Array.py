#https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

def removeDuplicate(arr):
    arr2=[]

    for i in range(len(arr)-1):
        if arr[i]!=arr[i+1]:
            arr2.append(arr[i+1])

    print(arr2)

removeDuplicate([1,1,2,3,5,6,7,8,9,9,9])

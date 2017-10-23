#https://leetcode.com/problems/search-for-a-range/description/

#Below is the old code
"""
def search_range(arr,start,end,item,rangeArray):
    print("I",end=" ")
    mid=int((start+end)/2)
    if start == end:
        return rangeArray
    if arr[mid]==item:
        if rangeArray[0]>mid:
            rangeArray[0] = mid
            search_range(arr,start,mid,item,rangeArray)
        if rangeArray[1]<mid:
            rangeArray[1] = mid
            search_range(arr, mid + 1, end, item, rangeArray)
        return rangeArray
    if arr[mid]>item:
        search_range(arr,start,mid,item,rangeArray)
        return rangeArray
    if arr[mid]<item:
        search_range(arr,mid+1,end,item,rangeArray)
    return rangeArray
rangeArray=[1000000,0]
input_arr=[7,7,7,7,7,7]
print(len(input_arr))
start=0
end=len(input_arr)-1
search_number=7
a=(search_range(input_arr,start,end,search_number,rangeArray))
print(a)
"""""
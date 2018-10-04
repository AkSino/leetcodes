def maxDiff(arr):

    rightMax=[0 for i in range(len(arr))]
    maxim=-1
    for i in range(len(arr)-1, -1, -1):
        maxim=max(maxim, arr[i])
        rightMax[i]=x


# Driver program to test above function
arr = [2, 3, 10, 2, 4, 8, 1]
size = len(arr)
print(size)

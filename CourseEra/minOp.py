def arraySum(arr, n):
    sm = 0
    i = 0
    while (i < n):
        sm = sm + arr[i]
        i = i + 1
    return sm

def smallest(arr, n):
    small = 1000000000
    for i in range(0, n):
        if (arr[i] < small):
            small = arr[i]
    return small

def countMoves(arr):
    n=len(arr)
    sm = arraySum(arr, n)
    small = smallest(arr, n)
    minOperation = sm - (n * small)
    return minOperation


print(countMoves([0,1,1,1,1]))
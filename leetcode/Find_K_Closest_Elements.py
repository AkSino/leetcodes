import bisect

def findClosestElements(arr, k, x):
    left = right = bisect.bisect_left(arr, x)
    while right - left < k:
        if left == 0: return arr[:k]
        if right == len(arr): return arr[-k:]
        print(x - arr[left - 1])
        print(arr[right] - x)
        if x - arr[left ] < arr[right+1] - x:
            left -= 1
        else:
            right += 1
    return arr[left:right]


print(findClosestElements([1,2,3,4,5,6,7],4,4))

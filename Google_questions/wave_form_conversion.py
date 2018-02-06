def sortInWave(arr, n):
    # Traverse all even elements
    for i in range(0, n, 2):

        # If current even element is smaller than previous, swap both of them
        if (i > 0 and arr[i] < arr[i - 1]):
            arr[i], arr[i - 1] = arr[i - 1], arr[i]

        # If current even element is smaller than next, swap both of them
        if (i < n - 1 and arr[i] < arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]


# Driver program
arr = [10, 90, 49, 2, 1, 5, 23]
sortInWave(arr, len(arr))
for i in range(0, len(arr)):
    print(arr[i])
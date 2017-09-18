# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
def merge(arr, starting_array, middle_elem, array_length):
    n1 = middle_elem - starting_array + 1
    n2 = array_length - middle_elem

    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[starting_array + i]

    for j in range(0, n2):
        R[j] = arr[middle_elem + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = starting_array  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, starting_array, array_length):
    if starting_array < array_length:
        # Same as (l+r)/2, but avoids overflow for
        # large l and h
        middle_elem = int((starting_array + (array_length - 1)) / 2)

        # Sort first and second halves
        mergeSort(arr, starting_array, middle_elem)
        mergeSort(arr, middle_elem + 1, array_length)
        merge(arr, starting_array, middle_elem, array_length)


# Driver code to test above
arr = [12, 11, 13, 5, 6, 7]
array_length = len(arr)
print("Given array is")
for i in range(array_length):
    print("%d" % arr[i]),

mergeSort(arr, 0, array_length - 1)
print("\n\nSorted array is")
for i in range(array_length):
    print("%d" % arr[i]),

    # This code is contributed by Mohit Kumra
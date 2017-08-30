array = [97, 200, 100, 101, 211, 107]


def partition(array, begin, end):
    x = array[end]
    i = begin - 1
    for j in range(begin, end - 1):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[end] = array[end], array[i + 1]
    return i + 1


def quick_sort(array, begin=0, end=None):
    if end is None:
        end = len(array) - 1

    def _quick_sort(array, begin, end):
        if begin >= end:
            return
        pivot = partition(array, begin, end)
        _quick_sort(array, begin, pivot - 1)
        _quick_sort(array, pivot + 1, end)

    return _quick_sort(array, begin, end)


quick_sort(array)
print(array)

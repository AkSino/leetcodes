class RadixSort(object):
    def __init__(self):
        pass
    def CSort(self, arrayToSort, m):
        n = len(arrayToSort)
        index_list = [0 for i in range(10)]
        main_data = [0 for i in range(n)]
        for i in range(n):
            position = (arrayToSort[i] / m)
            index_list[int((position) % 10)] += 1
        for i in range(1, 10):
            index_list[i] += index_list[i - 1]
        i = n - 1
        while i >= 0:
            position = int(arrayToSort[i] / m)
            main_data[index_list[int((position) % 10)] - 1] = arrayToSort[i]
            index_list[(position) % 10] =index_list[(position) % 10]- 1
            i =i- 1
        i = 0
        for i in range(len(arrayToSort)):
            arrayToSort[i] = main_data[i]
    def radixSort(self, output_array):
        if type(output_array[0])==str:
            res_array = [0 for i in range(len(output_array))]
            for i in range(len(output_array)):
                res_array[i] = ord(output_array[i])
            elem = max(res_array)
            n = 1
            while int(elem / n) > 0:
                self.CSort(res_array, n)
                n = n * 10
            for i in range(len(res_array)):
                res_array[i] = chr(res_array[i])
            return res_array
        else:
            elem = max(output_array)
            n = 1
            while int(elem / n) > 0:
                self.CSort(output_array, n)
                n = n * 10
            return output_array

arr = [23,4,133,12,45,32]
charArray=['c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f','c','d','a','m','f']
sortedList=RadixSort()
#int_sort=sortedList.radixSort(arr)
char_sort=sortedList.radixSort(charArray)
#print(int_sort)
print(char_sort)



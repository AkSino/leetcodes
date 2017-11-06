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
        elem = max(output_array)
        n = 1
        while int(elem / n) > 0:
            self.CSort(output_array, n)
            n = n * 10
        return output_array

    def RadixSort2(self, char_str):
        data_holder={}
        for i in range(len(char_str)):
            data_holder[ord(char_str[i])]=char_str[i]
            char_str[i]=ord(char_str[i])
        elem = max(char_str)
        n = 1
        while int(elem / n) > 0:
            self.CSort(char_str, n)
            n = n * 10
        for i in range(len(char_str)):
            char_str[i]=data_holder[char_str[i]]
        return char_str



arr = [23,4,133,12,45,32]
charArray=['c','b','a','m']
sortedList=RadixSort()
ans=sortedList.radixSort(arr)
char_ans=sortedList.charRadixSort(charArray)
print(ans)
print(char_ans)
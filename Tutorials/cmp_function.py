# Python Program to get the maximum
# possible integer from given array
# of integers...

# custom comparator to sort according
# to the ab, ba as mentioned in description
def comparator(a, b):
    ab = str(a) + str(b)
    ba = str(b) + str(a)
    return max(int(ba), int(ab))


# driver code
a = [54, 546, 548, 60, ]
sorted_array = sorted(a)
number = "".join([str(i) for i in sorted_array])
print(number)



a=[1, 34, 3, 98, 9, 76, 45, 4, 12, 121]
print(sorted(a,key=lambda x : x[1]))
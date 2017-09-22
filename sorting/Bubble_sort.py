#Bubble sort is just opposite of selection sort. We take the largest element to the rightmost element by keep comparing every two
#elements nearby.

arra=[7,9,4,1]
array_len=len(arra)-1

for j in range(array_len,0,-1):
    for i in range(array_len):
        if arra[i]>arra[i+1]:
            arra[i],arra[i + 1]=arra[i + 1],arra[i]


print(arra)



arr=[1,2,3,4]

for i in range(len(arr)):
    for j in range(i,len(arr)):
        arr[i],arr[j]=arr[j],arr[i]
        print(arr)
        arr[i], arr[j] = arr[j], arr[i]
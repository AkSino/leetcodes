arr=[0,1,0,0,0,0]
arr2=[]

for i in range(1,6):
    for j in range(1,i+2):
        arr2.append(arr[j-1]+arr[j])
    arr=[0]+arr2+[0]
    print(arr2)
    arr2=[]



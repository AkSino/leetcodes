int=100
arr=[]
while int!=0:
    if int%2==0:
        arr.append(0)
        int=int/2
    else:
        arr.append(1)
        int=int-1
        int=int/2

print(arr)
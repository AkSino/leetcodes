arr=["Thissssssssssss", "issss", "an", "example", "of", "text", "justification.","dude"]

linesp,backup=16,16
print_array=[]
flag=0
for i in range(len(arr)):
    linesp=linesp-len(arr[i])-flag
    if(linesp>=0):
        print_array.append(arr[i])
        if linesp-len(arr[i+1])-1>=0:
            print_array.append(" ")
            linesp=linesp-1
            flag=0
    else:
        residual_len=linesp+len(arr[i])
        limit=len(print_array)-2
        indexes=1
        while residual_len!=0 and len(print_array)!=1:
            print_array[indexes]=print_array[indexes] + " "
            indexes=(indexes+2)%limit
            residual_len=residual_len-1
        for m in print_array:
            print (m,end="")
        print()
        print_array=[]
        if(i!=len(arr)-1):
            linesp=backup-len(arr[i])
            print_array.append(arr[i])
            print_array.append(" ")
        else:
            print(arr[i])
        flag=1



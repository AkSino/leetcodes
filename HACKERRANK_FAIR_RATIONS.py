number=5
arr=[int(x) for x in input().split()]
odd=0
flag=0
for i in range(number):
    if(i==number-1) and (arr[i]&1):
        flag=1

    elif(arr[i]&1) and (i<number):
        odd+=1
        arr[i]+=1
        arr[i+1]+=1

    else:
        continue

if(flag==1):
    print ("NO")
else:
    print (odd*2)
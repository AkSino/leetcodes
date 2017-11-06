arr =[9,3,5,3,2,2,6,1,6,8,9]
i=0
itera=0
br=0
if len(arr)==1:
    print(0)
while i <= len(arr) and len(arr)!=1:
    max=0
    max_ind=0
    if br==1:
        print(itera)
        break
    for j in range(i+1, i+arr[i]+1):
        if j>=len(arr)-1:
            br=1
            break
        if arr[j]+j>max:
            max=arr[j]+j
            max_ind=j

    itera+=1
    i=max_ind
    max=0
    max_ind=0





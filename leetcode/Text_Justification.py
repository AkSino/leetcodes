arr=["Thiss", "iss", "an", "example", "of", "text", "justification.","dude"]
length=16
ans=0
a=[]
i=0
fin=[]
n=0
while ans<16:
    n+=1
    a.append(arr[i])
    ans+=len(arr[i])+(n-1)
    if ans>16:
        fin.append(a)
        ans=0
        n=0
    else:
        i+=1




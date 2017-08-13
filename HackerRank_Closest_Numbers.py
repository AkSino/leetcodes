num=int(input())
k=list(map(int, input().strip().split()))

k.sort()
s=0
for i in range(0,len(k)-1):
    if s==0:
        s=1
        mini=abs(k[i]-k[i+1])
    else:
        res=abs(k[i]-k[i+1])
        if res<mini:
            arra=[]
            mini=res
            arra.extend([k[i],k[i+1]])
            continue
        if res==mini:
            arra.extend([k[i],k[i+1]])
arra.sort()
print(*arra)





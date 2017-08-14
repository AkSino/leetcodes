j=int(input())
k=list(map(int, input().strip().split()))

k.sort(reverse=True)
reslut=0
for i in range(0,len(k)):
    reslut+=(k[i]*(2**i))

print(reslut)
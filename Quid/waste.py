n=1000
array=[2,5,7,9]

back=[False for i in range(n+1)]

for each in array:
    count=1
    while count*each<=n:
        back[count*each]=True
        count+=1

ans=0
for each in back:
    if each==False:
        ans+=1
print(len(back))
print(ans-1)
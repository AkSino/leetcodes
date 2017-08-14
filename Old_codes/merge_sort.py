a=[1,2,3,4,54,56,1000000]
b=[10,13,16,45,65,1000000]
c=[]
i=0
j=0

for len in range(0,11):
    if a[i]>b[j]:
        c.append(b[j])
        j+=1
    else:
        c.append(a[i])
        i+=1

print(c)

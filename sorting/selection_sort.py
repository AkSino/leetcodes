a=[4,2,5,1,4,8,3,6,2,9]

array_len=len(a)
for i in range(array_len-2):
    minimum=a[i]
    for j in range(i+1,array_len-1):
        if minimum>=a[j]:
            minimum=a[j]
            p=j
    a[p],a[i]=a[i],a[p]

print(a)

#Simply pick up one element and keep comparing it with other elemnt on remaining array.
#Pickup the minimum element and put it on the first position.




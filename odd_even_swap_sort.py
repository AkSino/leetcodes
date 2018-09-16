a=[1,3,5,6,3,3,3,8,2]

start=0
end=1

while end<len(a):
    if a[start]%2==1 and a[end]%2==0:
        a[start],a[end]=a[end],a[start]
        start+=1
        end+=1
    else:
        end+=1
print(a)

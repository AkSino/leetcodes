#https://leetcode.com/problems/median-of-two-sorted-arrays/description/

a=[1,2,3,4]
b=[2,2,4,5,6]

alen=len(a)
blen=len(b)
c=[]
i=0
j=0
while i<alen and j<blen:
    if a[i]<=b[j]:
        c.append(a[i])
        i+=1
    else:
        c.append(b[j])
        j+=1

if i==alen:
    c=c+b[j:blen]
if j==blen:
    c=c+a[i:alen]
print(c)

if len(c)%2==0:
    median=(c[len(c)//2]+c[(len(c)//2)-1])/2
else:
    median=(c[(len(c)//2)])

print(median)
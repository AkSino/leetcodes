import math
arr=[3,4,6,14,34,54,67]
key=54
if arr[0]==key:
    print(0)
i=1
while i<len(arr) and arr[i]<=key:
    i=i*2
if i>len(arr):
    ans=len(arr)
else:
    ans=i

for p in range(int(i/2),ans):
    print(arr[p])



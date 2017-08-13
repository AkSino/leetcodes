arr = list(map(int, input().strip().split(' ')))

arr.sort()

length=len(arr)

minsum=0
maxsum=0
base=0
for i in range(1,length-1):
    base=base+arr[i]
minsum=base+arr[0]
maxsum=base+arr[4]

print (minsum,maxsum)
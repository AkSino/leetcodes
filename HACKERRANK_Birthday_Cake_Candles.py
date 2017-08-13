n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

height.sort()

last=height[n-1]
count=0
for i in height:
    if (last==i):
        count+=1
print(count)
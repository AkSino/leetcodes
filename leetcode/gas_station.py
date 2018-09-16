gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

mid = []
left = [0]
sum = 0
right = [0 for i in range(len(gas))]
ans = None
for i in range(len(gas)):
    mid.append(gas[i] - cost[i])
left[0] = mid[0]
for i in range(1, len(mid)):
    left.append(left[-1] + mid[i])
right[-1] = mid[-1]
for i in range(len(mid) - 2, -1, -1):
    right[i] = right[i + 1] + mid[i]

print(mid)
print(left)
print(right)
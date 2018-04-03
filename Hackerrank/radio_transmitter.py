x=[1,2,3,4,5]
k=1

x.sort()
step = k
start = x[0] + step
count = 0
while start <= (max(x)+step):
    flag=True
    for i in range(start, start - step -1, -1):
        if i==x[start] or i==x[start-1]:
            count += 1
            flag=False
            break
    if flag:
        start = start + (step)
    else:
        start=i+(2*step)+1
print(count)

lines=[1,2,3,1,3,3,1,1]


stack=[0]
max_area=0

for i in range(1,len(lines)):
    if lines[i]>=lines[stack[-1]]:
        stack.append(i)
    else:
        while stack and lines[stack[-1]]>lines[i]:
            x=stack.pop(-1)
            if stack:
                max_area=max(max_area,(i-x)*lines[x])
            else:
                max_area=max(max_area,lines[x]*(i-x))
        stack.append(i)
while stack:
    p=stack.pop(-1)
    max_area=max(max_area,lines[p]*(i-p+1))
print(max_area)
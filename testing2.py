a=[[2,1],[1,9],[2,4],[2,6]]
c=[]
b=[]
for val,each in enumerate(a):
    b.append([each[1],val])
b=sorted(b)

for each in b:
    c.append(a[each[1]])

print(c)
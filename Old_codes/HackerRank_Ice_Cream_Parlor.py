m=[]
n=[]
p=[]
for i in range(int(input())):
    s=int(input())
    m.append(s)
    s = int(input())
    n.append(s)
    q=[]
    q=list(map(int, input().strip().split(' ')))
    p.append(q)

for i in range(len(m)):
    a=int(m[i])
    b=int(n[i])
    c=p[i]
    for k in range(len(c)-1):
        for j in range(k+1,len(c)):
            result=c[k] + c[j]
            if result==a:
                print(k+1,j+1)
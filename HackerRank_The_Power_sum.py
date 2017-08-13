def k(d,i):
    if d==0:
        return 1
    s=0
    j=i
    while not pow(j,n)>d:
        s+=k(d-pow(j,n),j+1)
        j+=1
    return s

x=int(input().strip())
n=int(input().strip())
print(k(x,1))
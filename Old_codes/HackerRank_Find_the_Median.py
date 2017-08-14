i=int(input())
k=list(map(int, input().strip().split()))

k.sort()
p=int(len(k)/2)
print (k[p])
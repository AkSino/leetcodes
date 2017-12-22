a=[1]
n=6
ans=[1,1]
for i in range(n-1):
    ans=[1] + [(ans[i-1]+ans[i]) for i in range(1,len(ans))] + [1]
    print(ans)




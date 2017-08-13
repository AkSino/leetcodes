def solve(n, ar, d, m):
    here_sum=0
    result=0
    for i in range(0,len(ar)-m+1):
        for j in range(i,i+m):
            here_sum+=ar[j]
        if here_sum==d:
            result+=1
        here_sum=0
    return result
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
d, m = input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, ar, d, m)
print(result)
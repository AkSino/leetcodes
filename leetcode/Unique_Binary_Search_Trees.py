def function(s,n):
    if(n<s):
        return 0
    if n==s:
        return 1

    ans=0
    for i in range(n,s-1,-1):
            ans+=function(1,i-1)+function(i+1,n)
    return ans

print(function(1,3))


def getRecord(s):
    maxi=s[0]
    mini=s[0]
    max_time=0
    min_time=0
    for i in range(1,len(s)):
        if s[i]>maxi:
            maxi=s[i]
            max_time+=1
        if s[i]<mini:
            mini=s[i]
            min_time+=1
    return (max_time,min_time)

n = int(input().strip())
s = list(map(int, input().strip().split(' ')))
result = getRecord(s)
print (" ".join(map(str, result)))
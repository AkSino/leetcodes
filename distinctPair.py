def numberOfPairs(a, k):
    dict={}
    repo=[]
    count=0
    if(len(a)==0):
        return 0
    for i in a:
        if (k-i) in dict:
            a=i
            b=k-i
            if(b>a):
                a,b=b,a
            if((a,b) not in repo):
                repo.append((a,b))
                count+=1
        dict[i]=1
    return count

print(numberOfPairs([1, 3, 46, 1, 3, 9], 47))


a=[(2,1),(1,1)]

a.sort()
print(a)
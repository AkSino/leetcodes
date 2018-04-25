def alternateMerging(array1,array2):
    if len(array1)>=len(array2):
        p1=array1
        p2=array2
    else:
        p1=array2
        p2=array1
    ans=[]
    for i in range(len(p2)):
        ans.append(p1[i])
        ans.append(p2[i])
    ans+=p1[len(p2):]
    return ans

print(alternateMerging([1,2],[2,"a"]))
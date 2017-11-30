a=["1","2","3"]
res=""
var=[]
def permutation(b,start,end,res):
    if start==end:
        return str(b[start])
    else:
        for i in range(len(b)):
            res=res+b[i]
            #print(b[start:i])
            #print(b[i:end])
            res=res+permutation(b[start:i]+b[i+1:end+1],0,end-1,res)
            return res
            var.append(res)
            res=""
    return (var)

print(permutation(a,0,2,res))
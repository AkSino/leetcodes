def calculate(x,y,maxim):
    i=0
    j=0
    maxi=0
    if len(x)==0 or len(y)==0:
        return maxim
    else:
        if x[i]==y[j]:
            maxim+=1
            maxi=calculate(x[1:len(x)],y[1:len(y)],maxim)
        else:
            p=calculate(x[1:len(x)],y,0)
            m=calculate(x,y[1:len(y)],0)
            maxi=max(p,maxim,m)

    return maxi

print(calculate([1,5,3],[1,3],0))
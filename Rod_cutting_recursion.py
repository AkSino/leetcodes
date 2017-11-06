def findMaxProf(Arr,lens):
    answer=[]
    if lens<=0:
        return 0,[]
    maxm=0
    for i in range(len(Arr)):
        if i<=lens:

            if(maxm<Arr[i]+ findMaxProf(Arr,lens-i-1)[0]):
                maxm=Arr[i]+ findMaxProf(Arr,lens-i-1)[0]
                answer=[i+1]+findMaxProf(Arr,lens-i-1)[1]
        else:
            return 0,[]
    return maxm,answer


print(findMaxProf([0,5,2,300,2],5))
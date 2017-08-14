def fourSum( num, target):
        n=len(num)
        D={}
        A=sorted(num)
        rst=[]
        for i in range(n-1):
            for j in range(i+1,n):
                psum=A[i]+A[j]
                if psum in D:
                    if [i,j] not in D[psum]:
                        D[psum]+=[[i,j]]
                else:
                    D[psum]=[[i,j]]
                if target-psum in D:
                    for elem in D[target-psum]:
                        if (i not in elem) and (j not in elem):
                            temp=sorted([A[i],A[j],A[elem[0]],A[elem[1]]])
                            if temp not in rst:
                                rst.append(temp)
        return rst

print (fourSum([1, 0, -1, 0, -2, 2], 0))
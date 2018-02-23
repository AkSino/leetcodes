from collections import defaultdict
def function(n,arrays):
    converting=defaultdict(int)
    arrays.sort(key=lambda x:x[1])
    count=0
    flag=True
    for i in arrays:
        flag=True
        if i[0]>=n:
            continue
        for j in range(i[0],i[1]):
            if j<n:
                if converting[j]<3:
                    continue
                else:
                    flag=False
                    break

        if flag:
            for j in range(i[0], i[1]):
                if j < n :
                    converting[j]+=1
            count+=1
    return count

import time
start = time.clock()
print(function(100000,[[5,6],[6,7]]))
print (time.clock() - start)
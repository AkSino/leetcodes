a=[[1,4],[2,6],[7,9],[11,14],[12,18]]
a.sort(key=lambda x:x[0])


result=[a[0]]
for i in range(1,len(a)):
    if a[i][0]<result[-1][1]:
        end=a[i][1]
        if a[i][1]<result[-1][1]:
            end=result[-1][1]
        result[-1][1]=end
    else:
        result.append(a[i])

print(result)
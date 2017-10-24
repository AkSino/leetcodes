arr1=[1,2,3,4]
arr2=[2,3,4,5]

arr1=list(arr1)
arr2=list(arr2)

result=arr1+arr2
result2=set(result)

for i in result2:
    result.remove(i)

print (result)



arr=[[[1,2,3]]]
arr[0].append([1,34,5])
print(arr)


arr1=[1,3,4]
arr2=[4,56,7]
x=[[]]
sys=[arr1,arr2]
for m in sys:
    x[0].append(m+[5])
print(x)
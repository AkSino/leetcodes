ar1 = [8,9,10]
ar2 = [1,2,3]


def medianSorted(arr1,arr2):

    if len(arr1)==1 and len(arr2)==1:
        return (arr2[0]+arr1[0])/2
    if len(arr1)==2 and len(arr2)==2:
        return (max(arr1[0],arr2[0])+min(arr1[1],arr2[1]))/2
    m1=median(arr1)
    m2=median(arr2)

    if m1==m2:
        return m1

    if m1>m2:
       return medianSorted(arr1[0:int(int(len(arr1))/2)+1],arr2[int(len(arr2)/2):len(arr2)])

    if m1<m2:
       return medianSorted(arr2[0:int(len(arr2)/2+1)],arr1[int(len(arr1)/2):len(arr1)])



def median(arr):
    n=len(arr)
    if len(arr)%2==0:
        return (arr[int(n/2)]+arr[int(n/2)-1])/2
    else:
        return arr[int(n/2)]

print(medianSorted(ar1, ar2))
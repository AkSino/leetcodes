def forSum(array):
    ans=0
    for each in array:
        ans+=each
    return ans

def whileSum(array):
    ans=0
    i=0
    while i<len(array):
        ans+=array[i]
        i+=1
    return ans

def recursionSum(array):
    return helperOfRecursion(array,0)

def helperOfRecursion(array,sum):
    if len(array)==1:
        return array[0]+sum
    else:
        return helperOfRecursion(array[1:],sum+array[0])

print(recursionSum([1]))
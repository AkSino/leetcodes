def ss(elements,target):
    if not  elements or len(elements)<=0:
        return -1
    left=0
    right=len(elements)-1
    while left<right:
        middle=(left+right+1)//2
        if elements[middle]>target:
            right=middle-1
        else:
            left=middle+1

    if elements[right]==target:
        return right
    return -1

print(ss([1,2,3,4,5],4))
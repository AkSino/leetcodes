def countMoves(numbers):
    return helper(numbers, 0)

def helper(numbers, steps):
    if(isEqual(numbers)):
        return steps
    skip = findIndex(numbers, max(numbers))
    array = increase(numbers,skip)
    return helper(array, steps + 1)

def isEqual(array):
    if(max(array)==min(array)):
        return True
    else:
        return False

def findIndex(array, target):
    for i in range(len(array)):
        if(array[i] == target):
            return i

def increase(array, skip):
    for i in range(len(array)):
        if(i!=skip):
            array[i]+=1
    return array

print(countMoves([0,1,1,1,1]))
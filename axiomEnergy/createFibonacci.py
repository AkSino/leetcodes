def printFibonacci():
    array=[0,1]
    for i in range(98):
        array.append(array[-1]+array[-2])
    return array
print(printFibonacci())

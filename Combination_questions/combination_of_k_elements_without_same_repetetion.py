input=[1,2,2,3,4,5]
input.sort()
start=0
def printCombination(input,array,k,elements,start):
    if k==elements:
        print(array)
        return
    for i in range(start,len(input)):
        if i>0 and input[i]==input[i-1] and k==0:
            continue
        array[k]=input[i]
        printCombination(input,array,k+1,elements,i+1)

printCombination(input,[0,0,0],0,3,start)
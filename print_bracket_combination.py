def printBracket(arr,position,open,close,n):
    if n==close:
        print(arr)
    else:
        if open>close:
            arr[position]="}"
            printBracket(arr,position+1,open,close+1,n)
        if open<n:
            arr[position]="{"
            printBracket(arr,position+1,open+1,close,n)

printBracket([0,0,0,0,0,0],0,0,0,3)
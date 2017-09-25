matrix=[[1,2,3,4,5],
        [16,17,18,19,6],
        [15,24,25,20,7],
        [14,23,22,21,8],
        [13,12,11,10,9]]
row_len=len(matrix)
col_len=len(matrix[0])



def printSpiral(a):
    row_len = len(a)
    col_len = len(a[0])
    row_str=0
    col_str=0
    d=0
    while(row_str<row_len and col_str<col_len):
        if(d==0):
            for i in range(col_str,col_len):
                print(a[row_str][i])
            row_str+=1
        if(d==1):
            for i in range(row_str,row_len):
                print(a[i][col_len-1])
            col_len-=1
        if(d==2):
            for i in range(col_len-1,col_str-1,-1):
                print(a[row_len-1][i])

            row_len-=1
        if(d==3):
            for i in range(row_len-1,row_str-1,-1):
                print(a[i][col_str])
            col_str+=1

        d=(d+1)%4


printSpiral(matrix)
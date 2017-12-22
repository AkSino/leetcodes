class Solution():
    def setZeroes(self,matrix):
        x=len(matrix)
        if x==0:
            return
        y=len(matrix[0])

        for i in range(x):
            for j in range(y):
                if matrix[i][j]==0:
                    for m in range(y):
                        if m<=j:
                            matrix[i][m]=0
                        if m>j and matrix[i][m]!=0 :
                            matrix[i][m]="*"
                    for n in range(x):
                        if n<=i:
                            matrix[n][j]=0
                        if n>i and matrix[n][j]!=0:
                            matrix[n][j]="*"
                if matrix[i][j]=="*":
                    matrix[i][j]=0
        return matrix
var=Solution()
print(var.setZeroes([[0,0,0,5],
                     [4,3,1,4],
                     [0,1,1,4],
                     [1,2,1,3],
                     [0,0,1,1]]))

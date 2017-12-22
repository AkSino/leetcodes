class Solution():
    def pacificAtlantic(self, matrix):
        ans=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):


    def Pacific(self,i,j,matrix):
        if i==0 or j==0:
            return True
        else:
            self.Pacific(i+1,j,matrix)
    def Atlantic(self,i,j,matrix):
        if (j==len(matrix[0]) or i==len(matrix)):
            return True

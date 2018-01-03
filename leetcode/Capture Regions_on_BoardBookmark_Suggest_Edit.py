class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        answer=[[1 for i in range(len(A[0]))] for j in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                if (i==len(A)-1 or i==0 or j==0 or j==len(A[0])-1) and A[i][j]==0:
                    self.helper(A,i,j,answer)
        return answer
    def helper(self,graph,i,j,answer):
        x=[0,0,-1,1]
        y=[1,-1,0,0]
        answer[i][j]=0
        graph[i][j]=3
        for m in range(len(x)):
            xx=x[m]
            yy=y[m]
            if  0<=i+xx<len(answer) and 0<=j+yy<len(answer[0]) and graph[i+xx][j+yy]==0:
                self.helper(graph,i+xx,j+yy,answer)

graph=[[1,1,1,1],
       [1,0,0,0],
       [1,1,0,1],
       [1,0,1,1]]

vardan=Solution()
print(vardan.solve(graph))
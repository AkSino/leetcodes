#https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, M):
        x=[1,1,-1,-1,0,0,1,-1]
        y=[1,-1,1,-1,1,-1,0,0]
        for i in range(len(M)):
            for j in range(len(M[0])):
                sums=0
                counter=0
                for m in range(len(x)):
                    if 0<=i+x[m]<len(M) and 0<=j+y[m]<len(M[0]):
                        sums+=M[i+x[m]][j+y[m]]
                        counter+=1
                M[i][j]=(sums+M[i][j])//(counter+1)
        return M

var=Solution()
print(var.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]))
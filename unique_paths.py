#This is a solution by recursion but this problem can be solved by using the mathematics as explained in the link
#https://leetcode.com/problems/unique-paths/discuss/22958


class Solution():
    def uniquePaths(self,m,n):
        a=[[None for i in range(n+1)] for j in range(m+1)]
        return self.uniquePath(m,n,a)
    def uniquePath(self,m,n,array):
        if array[m][n]:
            return array[m][n]
        if m==1 or n==1:
            return 1
        elif m==0 or n==0:
            return 0
        else:
            return self.uniquePath(m-1,n,array)+self.uniquePath(m,n-1,array)

var=Solution()
print(var.uniquePaths(3,3))
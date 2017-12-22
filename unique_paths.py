class Solution():
    def uniquePaths(self,m,n):
        if m==1 or n==1:
            return 1
        elif m==0 or n==0:
            return 0
        else:
            return max(m,n)*(min(m,n)-1)
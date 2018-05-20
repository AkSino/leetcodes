#https://leetcode.com/problems/combinations/description/

class Solution:
    def combine(self, n, k):
        ans=[]
        midAns=[None for  i in range(k)]
        array=[i for i in range(1,n+1)]
        self.helper(ans,array,k,0,len(array),midAns)
        return ans

    def helper(self,ans,array,n,start,end,midAns):
        if n==0:
            ans.append(list(midAns))
        else:
            for i in range(start,end-n+1):
                midAns[len(midAns)-n]=array[i]
                self.helper(ans,array,n-1,i+1,end,midAns)

var=Solution()
print(var.combine(3,3))


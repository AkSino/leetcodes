import math
class Solution:
    def Var(self, n, k):
        if len(n)==1:
            return n
        m=len(n)-1
        digit_reverse=(k-1)//math.factorial(m)

        if k<m:
            return [n[0]]+self.Var(n[1:len(n)],k)
        else:
            n[0],n[digit_reverse]=n[digit_reverse],n[0]
            k=k-(digit_reverse*math.factorial(m))
            return [n[0]]+ self.Var(sorted(n[1:len(n)]),k)
    def getPermutation(self,n,k):
        arr=[i for i in range(1,n+1)]
        p=self.Var(arr,k)
        return "".join(str(e) for e in p)

vaar=Solution()
print(vaar.getPermutation(4,13))
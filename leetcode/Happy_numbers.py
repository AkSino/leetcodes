from math import pow
class Solution:
    def isHappy(self, n):
        s=str(n)
        ans=0
        done=[]
        while True:
            if s in done:
                return False
            done.append(s)
            for each in s:
                ans=ans+int(pow(int(each),2))
            if ans==1:
                return True
            else:
                s=str(ans)
                ans=0

var=Solution()
print(var.isHappy(8))
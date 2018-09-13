class Solution:
    def grayCode(self, n):


    def calculateChars(self, n):
        chars=0
        while(n!=0):
            n=n//2
            chars+=1

    def returnValue(self, value):
        ans=0
        rep=0
        for i in range(len(value)-1, -1, -1):
            ans+=int(value[i])*(2**rep)
            rep+=1
        return ans
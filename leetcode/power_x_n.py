class Solution:
    def myPow(self, x, n):
        if n==2:
            return x**2
        elif n==1:
            return x
        elif n%2==1:
            return self.myPow(x,n//2)*x*self.myPow(x,n//2)
        else:
            return self.myPow(x,n/2)*self.myPow(x,n/2)


var=Solution()

print(var.myPow(4,4))
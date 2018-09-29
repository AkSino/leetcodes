class Solution(object):
    def climbStairs(self, n):

        if(n<=2):
            return n

        array = self.findFactorial(n)

        two = n // 2
        ans = 0
        for i in range(0, two + 1):
            ones=n-2*i
            twos=i

            ans+=array[ones+twos]//(array[ones]*array[twos])
        return ans

    def findFactorial(self, n):
        num = 1
        array = [1 for i in range(n + 1)]

        for i in range(1, n + 1):
            num = num * i
            array[i] = num
        return array

var=Solution()

print(var.climbStairs(3))
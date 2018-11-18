class Solution(object):
    def isHappy(self, n):
        a= set()

        if (n < 10):
            return self.isHappys(n * n, a)
        return self.isHappys(n, a)

    def isHappys(self, n, f):
        if(n in f):
            return False
        f.add(n)
        if (n < 10):
            if(n==1):
                return True
            return self.isHappys(n*n, f)
        result = 0
        while (n > 0):
            a = n % 10
            result += a * a
            n = n // 10
        return self.isHappys(result, f)


var = Solution()
print(var.isHappy(1111111))
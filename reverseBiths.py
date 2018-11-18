import math

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        g=31
        answer=0
        for i in range(32):
            i=n%2
            if(i==1):
                answer+=int(math.pow(2, g))
            n=n//2
            g-=1
        return answer


var=Solution()

print(var.reverseBits(123))
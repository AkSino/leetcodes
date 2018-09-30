class Solution(object):
    def isMonotonic(self, A):
        if(len(A)<=1):
            return True
        inc=0
        if(A[0]<A[1]):
            inc=1
        if(A[0]==A[1]):
            inc=2

        for i in range(1, len(A) - 1):
            x=0
            if(inc==2):
                if(A[i]<A[i+1]):
                    inc=1
                if(A[i]>A[i+1]):
                    inc=0
            if(A[i]<A[i+1]):
                x=1
            if(A[i]==A[i+1]):
                continue
            if(x!=inc):
                return False
        return True

var=Solution()
print(var.isMonotonic([1,1,2,0]))

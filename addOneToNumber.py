class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        sum = 0
        carry = 0
        start=0
        for i in range(len(A)-1,-1, -1):
            if(i==len(A)-1):
                sum = (1 + A[i]) % 10
                carry = (1 + A[i]) // 10
                if(sum!=0):
                    start=i
                A[i]=sum
            else:
                sum = (carry + A[i]) % 10
                carry = ( carry + A[i]) // 10
                if(sum!=0):
                    start=i
                A[i] = sum

        if (carry != 0):
            A.insert(0, carry)
        return A[start:len(A)]
var=Solution()
print(var.plusOne([ 0,0, 5 ]))
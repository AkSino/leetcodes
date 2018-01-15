class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 1
        ans_arr = []
        for i in range(len(A)-1, -1, -1):
            ans = carry
            carry = (A[i] + carry) // 10
            A[i] = (A[i] + ans) % 10
            if carry==0 and A[i]==0:
                last_index=i

        if carry:
            A.insert(0, carry)

        return A[last_index+1:]

var=Solution()
print(var.plusOne([9, 9, 8]))
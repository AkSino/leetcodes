#https://leetcode.com/problems/permutation-sequence/discuss/22614

# import math
# class Solution:
#     def Var(self, n, k):
#         if len(n)==1:
#             return n
#         m=len(n)-1
#         digit_reverse=(k-1)//math.factorial(m)
#
#         if k<m:
#             return [n[0]]+self.Var(n[1:len(n)],k)
#         else:
#             n[0],n[digit_reverse]=n[digit_reverse],n[0]
#             k=k-(digit_reverse*math.factorial(m))
#             return [n[0]]+ self.Var(sorted(n[1:len(n)]),k)
#     def getPermutation(self,n,k):
#         arr=[i for i in range(1,n+1)]
#         p=self.Var(arr,k)
#         return "".join(str(e) for e in p)
from math import factorial
class Solution(object):

    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        res = []
        nums = [i for i in range(1, n+1)]
        while n-1 >= 0:
            num, k = k//factorial(n-1), k % factorial(n-1)
            if k > 0:
                res.append(str(nums[num]))
                nums.remove(nums[num])
            else:
                res.append(str(nums[num-1]))
                nums.remove(nums[num-1])

            n -= 1

        return ''.join(res)

vaar=Solution()
print(vaar.getPermutation(4,13))
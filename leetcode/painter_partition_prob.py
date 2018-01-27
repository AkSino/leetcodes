#IT is a beautiful problem related to division of array in n parts such that maximum sum is minimum in that case.
#Here We will start from the middle of the sum and max value and see if we divide each partition in sum less than or equal to this sum, then how many partitions
#we will have. For example if we have a sum of 15 and we want to divide an array in 3 parts but taking 15 as sum we have only 2 arrays then obviously we can
#decrease the sum of each array.
#In this way it is a beautiful problem of binary search also.

# You have to paint N boards of length {A0, A1, A2, A3 … AN-1}. There are K painters available and you are also given how much time a painter takes to paint 1
#unit of board. You have to get this job done as soon as possible under the constraints that any painter will only paint contiguous sections of board.
#
# 2 painters cannot share a board to paint. That is to say, a board
# cannot be painted partially by one painter, and partially by another.
# A painter will only paint contiguous boards. Which means a
# configuration where painter 1 paints board 1 and 3 but not 2 is
# invalid.

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : list of integers
    # @return an integer
    def calcPainters(self, A, mid):
        total = 0
        painters = 1
        for x in range(len(A)):
            total = total + A[x]
            if total > mid:
                painters = painters + 1
                total = A[x]
        return painters

    def paint(self, k, t, C):
        s = sum(C)
        high = s
        low = max(C)
        while low < high:
            mid = int((high + low) / 2)
            requiredPainters = Solution.calcPainters(self, C, mid)
            if requiredPainters <= k:
                high = mid
            else:
                low = mid + 1
        return (low * t) % 10000003
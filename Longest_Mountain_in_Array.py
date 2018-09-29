class Solution:
    def longestMountain(self, A):
        switch = False
        length = 1
        max_l = 0
        if (len(A) < 3):
            return 0
        increase = A[0] < A[1]
        for i in range(1, len(A)):
            if (A[i] == A[i - 1]):
                switch = False
                length = 1
                if (i < len(A) - 1):
                    increase = A[i] < A[i + 1]
                continue
            if (increase and A[i] > A[i - 1]):
                length += 1
            elif ((increase) and A[i] < A[i - 1]):
                switch = True
                length += 1
                increase = False
                max_l = max(length, max_l)
            elif ((not increase) and A[i] < A[i - 1]):
                if (switch):
                    length += 1
                    increase = False
                    max_l = max(length, max_l)
            elif ((not increase) and A[i] > A[i - 1]):
                switch = False
                max_l = max(length, max_l)
                length = 2
                increase = True
        if (max_l >= 3):
            return max_l
        else:
            return 0


var = Solution()
print(var.longestMountain([2, 3, 3, 2, 0, 2]))

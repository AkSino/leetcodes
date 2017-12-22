class Solution:
    # @param A : integer
    # @return an integer
    def fibsum(self, A):
        fibs = [1, 1]
        while True:
            res = fibs[-1] + fibs[-2]
            if res > A:
                break
            else:
                fibs.append(res)
        count = 0
        i = -1
        while A > 0:
            num = fibs[i]
            if A >= num:
                count +=1
                A -= num
            i -= 1

        return int(count)

vardan=Solution()
print(vardan.fibsum(12))
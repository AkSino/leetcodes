#https://leetcode.com/problems/range-addition-ii/description/
class Solution:
    def maxCount(self, m, n, ops):
        count=m*n
        xmin=m
        ymin=n
        for each in ops:
            xmin=min(xmin,each[0])
            ymin=min(ymin,each[1])
        return xmin*ymin

var=Solution()
print(var.maxCount(40000,40000,[]))
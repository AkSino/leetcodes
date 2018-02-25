import sys
class Solution(object):
    def maxSubArray(self, nums):
        maximum_sum=-(sys.maxsize)
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>maximum_sum:
                maximum_sum=sum
            if sum<0:
                sum=0
        return maximum_sum

var=Solution()
print(var.maxSubArray([-1,2,3,-4,-2,-2]))
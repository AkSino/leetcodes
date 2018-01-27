#This is an classic example of how kdynamic programming works.
#Dynamic programming basically covers all the possible combinaitons in an array type of datastructue.
#In below example if we have to form 5 from 1,2,3 then it will check if 5 is formed with 1, then 4 is formed with 1 and so on. Then it will come on to
#2 and check if it is formed with


class Solution(object):
    # this is an application of knapsack problem, where w=sum(nums)/2
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        isum = sum(nums)

        # if weight not divisible by two, we cannot possibly have two equal sets
        if isum % 2 != 0:
            return False

        # isum is weight
        isum //= 2

        # dp init
        dp = [False for j in range(isum + 1)]
        dp[0] = True

        # j is weight bound, and i is arr pointer.
        # dp[j] :: for a weight j, can we partition into two equal sets with elements 0..i
        for i in range(len(nums)):
            # reversal neessary, because if we go in non-reversed order, we will overwrite
            # dp[] calculations from the previous iteration of outer loop. thus we go small to big to preserve previous iteration
            for j in reversed(range(1, isum + 1)):
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]

        return dp[isum]

var=Solution()
print(var.canPartition([2,2,6]))
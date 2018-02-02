class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        m = dict()
        m[0] = -1
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            if k != 0:
                sum = sum % k
            pre = m.get(sum)
            if pre is not None:
                if i - pre > 1: return True
            else:
                m[sum] = i
        return False


S = Solution()
print(S.checkSubarraySum([1,2,7], 7))
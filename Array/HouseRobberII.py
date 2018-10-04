class Solution(object):
    def rob(self, nums):
        if(len(nums)==0):
            return 0
        elif(len(nums)<3):
            return max(nums)

        dynamic = [0 for i in range(len(nums) + 2)]
        maxSum=0
        for i in range(2, len(dynamic)-1):
            dynamic[i] = max(nums[i - 2] + dynamic[i - 2], dynamic[i - 1])
            maxSum=max(maxSum, dynamic[i])

        dynamic = [0 for i in range(len(nums) + 2)]
        for i in range(3, len(dynamic)):
            dynamic[i] = max(nums[i - 2] + dynamic[i - 2], dynamic[i - 1])
            maxSum=max(maxSum, dynamic[i])
        return maxSum

var=Solution()
print(var.rob([1,2,1,1]))

class Solution:
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target

    def twoSum(self, nums, target):
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return (i, j)

a = list(map(int, input().strip().split(' ')))
n = int(input().strip())
emp1 = Solution()
vardan=emp1.twoSum(a,n)
print (vardan)

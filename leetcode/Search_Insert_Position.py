class Solution:
    def searchInsert(self,nums,target):
        n=len(nums)
        mid=n/2
        for i in range(len(nums)):
            if target==nums[i]:
                return i
            if target<nums[i]:
                return i
        return len(nums)


var=Solution()
print(var.searchInsert([1,3,5,6],7))
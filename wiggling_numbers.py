class Solution:
    def wiggleMaxLength(self, nums):
        ans=[nums[0]]
        first=nums[0]
        for i in range(1,len(nums)):
            if nums[i]>first:
                first=nums[i]
                ans.pop(len(ans)-1)
                ans.append(first)
            else:

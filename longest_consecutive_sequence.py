class Solution:
    def longestConsecutive(self, nums):
        nums=sorted(nums)

        if len(nums)==0:
            return 0
        a1=nums[0]
        count=1
        maxi=1
        for i in range(1,len(nums)):
            b1=nums[i]
            if b1==a1:
                continue
            if b1-a1==1:
                count+=1
                maxi = max(maxi, count)
            else:
                maxi=max(maxi,count)
                count=1
            a1=b1
        return maxi
var=Solution()
print(var.longestConsecutive([1,2,0,1]))

class Solution:
    def searchRange(self, nums, target):
        a=(self.firsthelper(nums,0,len(nums)-1,target))
        b=(self.lasthelper(nums, 0, len(nums) - 1, target))
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        else:
            return [-1,-1]
        if a and b:
            return [a,b]
        else:
            return [-1,-1]

    def firsthelper(self,nums,start,end,target):
        medium=(start+end)//2
        if start==end:
            if nums[start]==target:
                return start
            else:
                return None
        if nums[medium]<target:
            return self.firsthelper(nums,medium+1,end,target)
        elif nums[medium]>target:
            return self.firsthelper(nums,start,medium-1,target)
        else:
            if medium==0 and nums[medium]==target:
                return medium
            else:
                if nums[medium-1]<target:
                    return medium
                else:
                    return self.firsthelper(nums,start,medium-1,target)

    def lasthelper(self,nums,start,end,target):
        if start==end:
            if nums[start]==target:
                return start
            else:
                return None
        medium=(start+end)//2
        if nums[medium]<target:
            return self.lasthelper(nums,medium+1,end,target)
        elif nums[medium]>target:
            return self.lasthelper(nums,start,medium-1,target)
        else:
            if medium==(len(nums)-1) and nums[medium]==target:
                return medium
            else:
                if nums[medium+1]>target:
                    return medium
                else:
                    return self.lasthelper(nums,medium+1,end,target)

var=Solution()
print(var.searchRange([5,7,7,8,8,10],8))
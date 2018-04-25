#https://leetcode.com/problems/search-for-a-range/description/

class Solution:
    def searchRange(self, nums, target):
        print(self.helperFirst(0,len(nums)-1,nums,target))
    def helperFirst(self,start,end,array,target):
        if start==end:
            if array[start]==target:
                return start
            else:
                return -1
        mid=(start+end)//2
        if ((array[mid]==target and mid==0) or (array[mid]==target and array[mid]>array[mid-1])):
            return mid
        elif array[mid]>target:
            return self.helperFirst(start,mid-1,array,target)
        elif array[mid]<target:
            return self.helperFirst(mid+1,end,array,target)
        else:
            return self.helperFirst(start,mid-1,array,target)
    def helperLast(self,start,end,array,target):
        pass

var=Solution()
var.searchRange([0,1,1],1)
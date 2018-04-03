#https://leetcode.com/problems/increasing-subsequences/description/
from copy import deepcopy

class Solution:
    def findSubsequences(self, nums):
        finans=[]
        midarray=[]
        for n in range(2,len(nums)+1):
            for i in range(len(nums)):
                if len(midarray)>1:
                    finans.append(midarray)
                midarray=[nums[i]]
                if i+n<=len(nums):
                    for j in range(i+1,i+n):
                        if midarray[-1]<nums[j] and midarray+[]:
                            midarray.append(nums[j])
        print(finans)

var=Solution()
var.findSubsequences([1,6,3,4])


# class Solution:
#     def findSubsequences(self, nums):
#         return (self.helper(nums,[],[],0))
#
#     def helper(self,nums,finans,midans,index):
#         if len(midans)>1 and midans not in finans:
#             finans.append(midans)
#         for i in range(index,len(nums)):
#             if len(midans)>0:
#                 if midans[-1]<=nums[i]:
#                     self.helper(nums,finans,midans+[nums[i]],i+1)
#             else:
#                 self.helper(nums, finans, midans + [nums[i]], i + 1)
#         return finans
#
# var=Solution()
# var.findSubsequences([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
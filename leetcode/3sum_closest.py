#https://leetcode.com/problems/3sum-closest/description/
class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        diff = 9999999
        for k in range(len(nums)-2):
            i = 0
            j = len(nums)-1

            ans=target-nums[k]
            while i<j:
                if(i==k):
                    i+=1
                    continue
                if (j == k):
                    j -= 1
                    continue
                if ans==nums[i]+nums[j]:
                    mer = [nums[i], nums[j], nums[k]]
                    return mer
                if ans>nums[i]+nums[j]:

                    if diff>abs(ans-(nums[i]+nums[j])):
                        mer=[nums[i],nums[j],nums[k]]
                        diff = min(diff, abs(ans - (nums[i] + nums[j])))
                    i=i+1
                else:
                    if diff>abs(ans-(nums[i]+nums[j])):
                        mer=[nums[i],nums[j],nums[k]]
                        diff = min(diff, abs(ans - (nums[i] + nums[j])))
                    j=j-1
        return sum(mer)

var=Solution()
print(var.threeSumClosest([-3,0,1,2],1))
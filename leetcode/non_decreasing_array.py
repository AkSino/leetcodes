#https://leetcode.com/problems/non-decreasing-array/description/
class Solution:
    def checkPossibility(self, nums):
        nums.insert(0,-100000)
        count = 0
        for i in range(1, len(nums)-1):
            if nums[i] > nums[i + 1]:
                    if (nums[i - 1] ) <= nums[i + 1]:
                        count += 1
                        if count==2:
                            return False
                        nums[i]=nums[i-1]
                    else:
                        count += 1
                        if count==2:
                            return False
                        nums[i+1]=nums[i]
        return True
var=Solution()
print(var.checkPossibility([1,2,4,1,6,7]))


#[7,8,2,11,12]
#[1,2,4,1,6,7]

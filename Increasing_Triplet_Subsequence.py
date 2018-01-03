import sys

class Solution:
    def increasingTriplet(self, nums):
        min1=sys.maxsize
        min2=sys.maxsize

        for i in range(0,len(nums)):
            current=nums[i]

            if (min1>=current):
                min1=current
            elif min2>=current:
                min2=current
            else:
                return True
        return False

var=Solution()
print(var.increasingTriplet([1,2,3]))

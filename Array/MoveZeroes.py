class Solution(object):
    def moveZeroes(self, nums):

        if(len(nums)<2):
            return

        i = 1
        j = 0

        while (i < len(nums)):
            if (nums[j] == 0):
                if (nums[i] != 0):
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
                    j += 1
                else:
                    i += 1
                continue
            elif (nums[j] != 0):
                j += 1
                i += 1

var=Solution()

var.moveZeroes([1,0,3,0,0])


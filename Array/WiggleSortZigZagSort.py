class Solution(object):
    def wiggleSort(self, nums):
        if (len(nums) <= 1):
            return nums

        for i in range(1, len(nums)):
            if(i%2==0):
                pass
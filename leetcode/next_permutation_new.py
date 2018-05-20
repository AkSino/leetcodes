class Solution:
    def nextPermutation(self, nums):
        if len(nums)<=1:
            return
        array=[]
        breakpoint=0
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                breakpoint=i
                break
        if breakpoint==0:
            nums.reverse()
        else:
            swp1=breakpoint-1
            swp2=breakpoint
            for p in range(breakpoint,len(nums)):
                if nums[breakpoint-1]<nums[p]:
                    swp2=p
            nums[swp2],nums[swp1]=nums[swp1],nums[swp2]

            array=nums[breakpoint:len(nums)]
            array.sort()
            for i in range(breakpoint,len(nums)):
                nums[i]=array[i-breakpoint]

arraya=[1,3,2]
var=Solution()
var.nextPermutation(arraya)
print(arraya)
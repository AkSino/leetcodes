class Solution:
    def nextPermutation(self, nums):
        stop=0
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                stop=i+1
                break
        if stop==0:
            nums.reverse()
        else:
            subarray=nums[i+1:len(nums)]
            subarray.sort()
            for elem in range(len(subarray)):
                if subarray[elem]>nums[stop-1]:
                    elems=subarray[elem]
                    subarray[elem]=nums[stop-1]
                    subarray.sort()
                    break
            nums[stop-1]=elems
            nums[stop:len(nums)]=subarray
        return nums

var=Solution()
print(var.nextPermutation([1,3,2]))



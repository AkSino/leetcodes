class Solution:
    def jump(self, nums):
        l = len(nums)
        fuel = nums[0]
        min_steps = 0
        start=1
        maxim=0
        max_ind=0
        flag=True
        while(fuel>0 and start<len(nums)):
            if(flag):
                min_steps+=1
                flag=False
            if(maxim<nums[start]+start):
                maxim=nums[start]+start
                max_ind=start
            if(start==len(nums)-1):
                break
            start+=1
            fuel-=1
            if(fuel==0):
                fuel=nums[max_ind]-start+max_ind+1
                flag=True
        return min_steps


var=Solution()
print(var.jump([1,1,1]))

class Solution():
    def canJump(self,nums):

        if len(nums)==1:
            return True
        steps=nums[0]
        maxim=0
        if steps==0:
            return False
        for i in range(1,len(nums)):
            maxim=max(maxim,i+nums[i])
            steps-=1
            if i==len(nums)-1:
                return True
            if steps==0:
                steps=maxim-i
                if steps<=0:
                    return False

var=Solution()
print(var.canJump([2,0,0,0]))

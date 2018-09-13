class Solution:
    def trap(self, height):
        leftStack=[]
        rightStack=[]
        ans=0
        for i in range(len(height)):
            if(not leftStack):
                if(height[i]!=0):
                    leftStack.append(i)

            else:
                if(height[i]>=height[leftStack[0]]):
                    while(leftStack):
                        ans += height[leftStack[0]] - height[leftStack.pop(-1)]
                    leftStack.append(i)
                else:
                    leftStack.append(i)
        if(len(leftStack)>1):
            rMax=leftStack[-1]
            p=len(leftStack)-2
            while(p>=0):
                if(height[leftStack[p]]>height[rMax]):
                    rMax=leftStack[p]
                    p-=1
                else:
                    ans+=height[rMax]-height[leftStack[p]]
                    p-=1
        return ans




var=Solution()
print(var.trap([4,3,3,9,3,0,9,2,8,3]))
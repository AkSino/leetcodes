class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        if(len(nums)==0):
            return None
        return self.helperFunction(nums, 0, len(nums)-1)

    def helperFunction(self, nums, start, end):

        if(start==end):
            return TreeNode(nums[start])
        elif(start>end or start<0 or end>=len(nums)):
            return
        maxNum=-1
        index=-1
        for i in range(start, end+1):
            if(maxNum<nums[i]):
                maxNum=nums[i]
                index=i

        node=TreeNode(maxNum)
        node.left=self.helperFunction(nums, start, index-1)
        node.right=self.helperFunction(nums, index+1, end)

        return node


var=Solution()
p=var.constructMaximumBinaryTree([3,2,1,6,0,5])
print(p)
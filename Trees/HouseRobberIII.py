from MyLibrary import TreeLibrary

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        return self.helperFunction(root, 0, 0)

    def helperFunction(self, root, lastSum, lastToLastSum):
        if(root==None):
            return max(lastSum, lastToLastSum)

        maxim=max(lastSum, lastToLastSum + root.val)

        return (self.helperFunction(root.left, maxim, lastSum) + self.helperFunction(root.right, maxim, lastSum))

root=TreeLibrary.arrayToTree([3,2,3,None,3,None,1])
var=Solution()
print(var.rob(root))
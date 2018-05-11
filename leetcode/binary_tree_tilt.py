class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root):
        if root==None:
            return 0
        return self.helperFunction(root,[0])[1][0]

    def helperFunction(self,root,array):
        left=0
        right=0
        if root.left:
            left=root.left.val+self.helperFunction(root.left,array)[0]
        if root.right:
            right=root.right.val+self.helperFunction(root.right,array)[0]

        array[0]=array[0]+abs(left-right)
        return ((left+right),array)

var=TreeNode(1)
var.left=TreeNode(2)
#var.left.right=TreeNode(2)
var.right=TreeNode(3)
#var.right.right=TreeNode(4)
#var.right.right.left=TreeNode(4)
sol=Solution()
print(sol.findTilt(var))

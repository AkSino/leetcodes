class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rightSideView(self, root):
        return self.helperFunction(root, [], 0)

    def helperFunction(self, root, array, level):
        if(root==None):
            return
        if(level==len(array)):
            array.append(root.val)
        self.helperFunction(root.right, array, level+1)
        self.helperFunction(root.left, array, level+1)
        return array

x=TreeNode(1)
x.right=TreeNode(2)
x.right.right=TreeNode(3)

var=Solution()
print(var.rightSideView(x))
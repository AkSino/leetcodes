class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        return self.helperFunction(root, -float('inf'), float('inf'))
    def helperFunction(self, root, minimum , maximum):
        if(root==None):
            return True
        if(root.val>=maximum or root.val<=minimum):
            return False
        else:
            return (self.helperFunction(root.left, minimum, root.val) and self.helperFunction(root.right, root.val, maximum))

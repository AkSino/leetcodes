class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root):
        if root==None:
            return True
        return (self.mirror(root.left, root.right))

    def mirror(self,left, right):
        if left is None and right is None:
            return True

        if left is None or right is None:
            return False

        if left.val != right.val:
            return False

        return (self.mirror(left.left, right.right) and self.mirror(left.right, right.left))

var=TreeNode(1)
var.left=TreeNode


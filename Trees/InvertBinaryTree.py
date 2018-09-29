class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        if(root==None):
            return None
        else:
            root.right, root.left=root.left, root.right
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
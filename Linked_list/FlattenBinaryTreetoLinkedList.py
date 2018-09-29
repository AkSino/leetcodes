class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def flatten(self, root):
        self.flattens(root)
    def flattens(self, root):
        if (root == None):
            return None
        if (not root.right and not root.left):
            return root
        right=None
        left=None
        if (root.right):
            right = self.flattens(root.right)
        if (root.left):
            left = self.flattens(root.left)

        if(left):
            root.left=None
            root.right = left
            x=root
            while(x.right):
                x=x.right
            x.right = right
            return root
        else:
            root.left=None
            root.right=right
            return root


var=Solution()
tree=TreeNode(1)
tree.left=TreeNode(2)
tree.left.left=TreeNode(3)
tree.left.right=TreeNode(4)
tree.right=TreeNode(5)
tree.right.right=TreeNode(6)


a=var.flatten(tree)
print(a)
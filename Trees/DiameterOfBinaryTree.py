class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        return self.helperFunction(root, 0)

    def helperFunction(self, root, height):
        if (root == None):
            return [height, 0]
        left = self.helperFunction(root.left, height + 1)[0]
        right = self.helperFunction(root.right, height + 1)[0]
        left_self = left - height
        right_self = right - height
        return [max(left, right), left_self + right_self]

var=Solution()
a=TreeNode(1)
a.left=TreeNode(2)
a.right=TreeNode(3)
a.left.right=TreeNode(2)
a.left.left=TreeNode(2)
a.left.right.right=TreeNode(2)
a.left.right.right.right=TreeNode(2)
print(var.diameterOfBinaryTree(a)[0])




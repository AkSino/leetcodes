class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None
        indices = {val: i for i, val in enumerate(inorder)}
        return self.build(indices, 0, len(inorder), inorder, postorder)

    def build(self, indices, low, high, inorder, postorder):
        if low == high or not postorder:
            return None

        root = TreeNode(postorder.pop())
        mid = indices[root.val]
        root.right = self.build(indices, mid + 1, high, inorder, postorder)
        root.left = self.build(indices, low, mid, inorder, postorder)
        return root


inorder = [9, 3, 15, 20, 7]
postorder = [9, 15, 7, 20, 3]

var = Solution()
var.buildTree(inorder, postorder)

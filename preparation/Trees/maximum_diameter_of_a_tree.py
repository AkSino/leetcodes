class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None


class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.best = 1

        def depth(root):
            if not root: return 0
            ansL = depth(root.left)
            ansR = depth(root.right)
            self.best = max(self.best, ansL + ansR + 1)
            return 1 + max(ansL, ansR)

        depth(root)
        return self.best - 1
tree=Node(1)
tree.right=Node(2)
tree.left=Node(3)
tree.right.right=Node(5)
tree.left.right=Node(4)

var=Solution()
print(var.diameterOfBinaryTree(tree))
class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class Solution():
    def invertTree(self,root):
        if root==None:
            return
        root.left,root.right=root.right,root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

tree=Node(1)
tree.right=Node(2)
tree.left=Node(3)
tree.right.right=Node(5)
tree.left.right=Node(4)

var=Solution()
tree=var.invertTree(tree)

print(tree.data)
print(tree.right.data)
print(tree.left.data)
print(tree.right.right.data)
print(tree.left.right.data)


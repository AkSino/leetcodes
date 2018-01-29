class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution():
    def printHeight(self,root,n):
        if root==None:
            return n
        else:
            return max(self.printHeight(root.right,n+1),self.printHeight(root.left,n+1))

tree=Node(1)
tree.right=Node(2)
tree.left=Node(3)
tree.right.right=Node(5)
tree.left.right=Node(4)

var=Solution()
print(var.printHeight(tree,0))
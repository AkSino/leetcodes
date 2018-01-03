class Node:
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def rightSideView(self, root):
        if root==None:
            return
        print(root.key)
        if root.right:
            self.rightSideView(root.right)
        elif root.left:
            self.rightSideView(root.left)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

var=Solution()
var.rightSideView(root)


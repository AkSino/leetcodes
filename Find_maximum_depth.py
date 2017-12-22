class Node:
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root):
        if root == None:
            return 0
        else:
            depth = min(1 + self.minDepth(root.left), 1 + self.minDepth(root.right))
        return depth



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
print(findMinDepth(root))
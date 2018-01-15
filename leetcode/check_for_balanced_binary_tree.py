class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

def checkBalance(root):
    if root==None:
        return 0
    right=checkBalance(root.right)
    left=checkBalance(root.left)

    if left==-1 or right==-1 or abs(left-right)>1:
        return -1
    else:
        return 1 + max(left,right)
tree=Node(5)
tree.left=Node(3)
tree.right=Node(7)
tree.left.left=Node(3)
tree.left.right=Node(3)
tree.right.left=Node(3)
tree.right.right=Node(37)
print(checkBalance(tree))
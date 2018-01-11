class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def frequentSubtree(root):
    if root==None:
        return [0]
    ans=[root.data+frequentSubtree(root.left)[0]+frequentSubtree(root.right)[0],frequentSubtree(root.left)[0],frequentSubtree(root.right)[0]]

    return ans


tree=Node(2)
tree.right=Node(3)
tree.left=Node(4)
tree.left.left=Node(3)
tree.left.right=Node(4)
tree.right.left=Node(7)
tree.right.right=Node(5)
print(frequentSubtree(tree))
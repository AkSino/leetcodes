class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution:
    def widthOfBinaryTree(self, root):
        queue=[(root,0,0)]
        while queue:
            a=queue.pop()
            node=a[0]
            index=a[1]
            depth=a[2]
            queue.append(node.left,index,depth+1)
            queue.append(node.left, index + 1, depth + 1)





root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
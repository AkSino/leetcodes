class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Solution():
    def findDiameter(self,root):
        if root==None:
            #here first is diameter and second is the depth
            return [0,0]
        else:
            ldata=self.findDiameter(root.left)
            rdata=self.findDiameter(root.right)

            diameter=max(ldata[0],rdata[0],ldata[1]+rdata[1]+1)
            return [diameter,max(ldata[1],rdata[1])+1]

tree=Node(1)
tree.left=Node(2)
tree.right=Node(3)
tree.right.right=Node(4)
tree.right.right.right=Node(6)
tree.right.left=Node(5)
tree.right.left.left=Node(7)

var=Solution()
print(var.findDiameter(tree))
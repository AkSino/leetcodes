class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Solution():
    def findElement(self,root,k,array):
        if root==None:
            return 0
        else:
            a=self.findElement(root.left,k,[array[0]+1])
            b=self.findElement(root.right,k)

            if k==a+b+1:
                print(root.data)

tree=Node(2)
tree.right=Node(3)
tree.left=Node(1)

var=Solution()
var.findElement(tree,1)

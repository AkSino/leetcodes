class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Solution():
    def  __init__(self,number):
        self.num=number
    def findElement(self,root):
        if root==None:
            return
        else:
            b=self.findElement(root.left)
            self.num-=1
            if self.num==0:
                return root.data
            a=self.findElement(root.right)
        return (a or b)


tree=Node(2)
tree.right=Node(3)
tree.left=Node(1)
tree.left.right=Node(1.5)

var=Solution(2)
print(var.findElement(tree))

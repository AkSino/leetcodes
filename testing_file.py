class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None



class Solution():
    def Ksum(self,root,sum,k):
        if root:
            if sum+root.data==k or self.Ksum(root.left,sum+root.data,k) or self.Ksum(root.right,sum+root.data,k):
                return True
        else:
            return False



root=Node(2)
root.left=Node(4)
root.right=Node(5)
root.left.left=Node(28)
root.left.right=Node(23)
root.right.left=Node(19)
root.right.right=Node(11)

var=Solution()
print(var.Ksum(root,0,16))



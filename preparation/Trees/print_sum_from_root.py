class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution():
    def printSum(self,root,n,array,sum):

        if root==None:
            return
        if len(array) >= n + 1:
            array[n] = root.data
        else:
            array.append(root.data)
        if sum-root.data== 0:
            print(array[0:n+1])
        else:
            self.printSum(root.right,n+1,array,sum-root.data)
            self.printSum(root.left,n+1,array,sum-root.data)



tree=Node(1)
tree.right=Node(2)
tree.left=Node(3)
tree.right.right=Node(5)
tree.left.right=Node(4)

var=Solution()
var.printSum(tree,0,[],8)
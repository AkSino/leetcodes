class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Solution():
    def printSum(self,root,n,array,sum):
        tmp=sum
        if root==None:
            return
        else:
            if len(array)>=n+1:
                array[n]=root.data
            else:
                array.append(root.data)
            for item in range(n,-1,-1):
                sum-=array[item]
                if sum==0:
                    print(array[item:n+1])
            self.printSum(root.right,n+1,array,tmp)
            self.printSum(root.left,n+1,array,tmp)

tree=Node(1)
tree.right=Node(2)
tree.left=Node(3)
tree.right.right=Node(5)
tree.left.right=Node(4)

var=Solution()
var.printSum(tree,0,[],7)
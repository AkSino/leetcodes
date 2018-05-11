class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def printBranch(root,array,n):
    if root.left==None and root.right==None:
        if len(array)<=n:
            array.append(root.val)
        else:
            array[n]=root.val
        print(array[0:n+1])
    else:
        if len(array)<=n:
            array.append(root.val)
        else:
            array[n]=root.val
        if root.right:
            printBranch(root.right,array,n+1)
        if root.left:
            printBranch(root.left,array,n+1)

var=TreeNode(1)
var.left=TreeNode(2)
var.left.right=TreeNode(2)
var.right=TreeNode(3)
var.right.right=TreeNode(4)
var.right.right.left=TreeNode(4)

printBranch(var,[],0)
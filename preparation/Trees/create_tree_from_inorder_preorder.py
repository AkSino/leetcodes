preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

class Tree():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def prepareTree(inorder,preorder):
    if inorder:
        ind = inorder.index(preorder.pop(0))
        root=Tree(inorder[ind])
        root.left=prepareTree(inorder[0:ind],preorder)
        root.right=prepareTree(inorder[ind+1:],preorder)
        return root
    return

def printInorder(root):
    if root==None:
        return
    printInorder(root.left)
    print(root.data)
    printInorder(root.right)

a=prepareTree(inorder,preorder)
printInorder(a)
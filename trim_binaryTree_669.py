class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root, L, R):
        if root==None:
            return
        elif root.val>R:
            return self.trimBST(root.left,L,R)
        elif root.val<L:
            return self.trimBST(root.right,L,R)
        elif root.val>=L and root.val<=R:
            root.right=self.trimBST(root.right,L,R)
            root.left=self.trimBST(root.left,L,R)
            return root

t1=TreeNode(2)
t1.right=TreeNode(3)
t1.left=TreeNode(1)
t1.left.left=TreeNode(0)

var=Solution()
x=var.trimBST(t1,0,1)
print(x.val)

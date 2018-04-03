class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def mergeTrees(self, t1, t2):
        if not t1 and not t2:
            return
        if t1 and t2:
            x=TreeNode(t1.val+t2.val)
            x.left=self.mergeTrees(t1.left,t2.left)
            x.right=self.mergeTrees(t1.right,t2.right)
        else:
            if t1:
                x=TreeNode(t1.val)
                x.right=self.mergeTrees(t1.right,None)
                x.left=self.mergeTrees(t1.left,None)
            elif t2:
                x=TreeNode(t2.val)
                x.right=self.mergeTrees(t2.right,None)
                x.left=self.mergeTrees(t2.left,None)
        return x

t1=TreeNode(1)
t1.right=TreeNode(2)
t1.left=TreeNode(3)
t1.left.left=TreeNode(5)

t2=TreeNode(2)
t2.right=TreeNode(3)
t2.left=TreeNode(1)
t2.left.right=TreeNode(4)
t2.right.right=TreeNode(7)

var=Solution()
x=var.mergeTrees(t1,t2)
print(x.val)
print(x.right.val)
print(x.left.val)
print(x.left.right.val)
print(x.left.left.val)
print(x.right.right.val)
print(x.right.left)
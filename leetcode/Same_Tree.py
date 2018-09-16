class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if not p and not q:
            return True
        else:
            if p is not None and q is None:
                return False
            elif p is None and q is not None:
                return False
            elif p.val==q.val and p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right):
                return True
            else:
                return False


var=Solution()



#Find minimum difference between any pair of node and its child

class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

class Solution():
    def getMinimumDifference(self, root):
        arr=[root]
        minDiff=100000000000000000
        while arr:
            elem=arr.pop(0)
            if elem.left:
                minDiff=min(minDiff,abs(elem.val-elem.left.val))
                arr.append(elem.left)
            if elem.right:
                minDiff=min(minDiff,abs(elem.val-elem.right.val))
                arr.append(elem.right)

        return minDiff


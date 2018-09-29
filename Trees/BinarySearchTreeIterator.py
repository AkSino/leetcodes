class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.trav = root
        self.stack = []

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.trav or self.stack

    def next(self):
        """
        :rtype: int
        """

#Concept that we are using here is that we will keep on adding all the left nodes to the stack. After we reach on to the leaf, we will basically pop the last one
#and print it. Then we make u as the next right element. When on the leaf element it will not find any right element, it will pop the root node of leaf,
#then print it. Then we do the same procedure on the lest side of the right node. This will serve the purpose.
        while self.trav:
            self.stack.append(self.trav)
            self.trav = self.trav.left
        u = self.stack.pop()
        self.trav = u.right
        return u.val

root=TreeNode(15)
root.left=TreeNode(8)
root.right=TreeNode(100)
root.left.left=TreeNode(5)
root.left.right=TreeNode(10)
root.left.left.left=TreeNode(3)
root.left.left.right=TreeNode(6)

var=BSTIterator(root)
print(var.next())
print(var.next())
print(var.next())
print(var.next())

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        self.helperFunction(root)


    def helperFunction(self, root):
        if(root==None):
            return
        root.left.next=root.right
        if(root.next):
            root.right.next=root.next.left
        self.helperFunction(root.left)
        self.helperFunction(root.right)
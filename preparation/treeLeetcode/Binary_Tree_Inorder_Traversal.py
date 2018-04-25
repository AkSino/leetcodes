#https://leetcode.com/problems/binary-tree-inorder-traversal/description/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderTraversal(self, root):
        if root==None:
            return []
        return(self.helper(root,[]))
    def helper(self,root,array):
        if root==None:
            return
        self.helper(root.left,array)
        array.append(root.val)
        self.helper(root.right,array)
        return array
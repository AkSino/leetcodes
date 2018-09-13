class Solution:
    def increasingBST(self, root):
        array=[]
        self.helperFunction(root, array)
        if(len(array)==0):
            return None

        root=TreeNode(array[0])
        retu = root
        for i in range(1, len(array)):
            root.right=TreeNode(array[i])
            root=root.right
        return retu

    def helperFunction(self, root, array):
        if(root==None):
            return
        self.helperFunction(root.left, array)
        array.append(root.val)
        self.helperFunction(root.right, array)
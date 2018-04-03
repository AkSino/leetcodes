class TreeNode:
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None
class Solution():
    def helper(self,root,value,nas):
        if root==None:
            return
        else:
            self.helper(root.left,value,nas)
            if len(value)!=0:
                nas[0]=min(nas[0],abs(root.val-value[-1]))
                value.append(root.val)
                self.helper(root.right,value,nas)
            else:
                value.append(root.val)
                self.helper(root.right,value,nas)
        return nas[0]

    def getMinimumDifference(self, root):
        nas=[1000000000]
        value=[]
        return self.helper(root,value,nas)


node=TreeNode(2)
node.right=TreeNode(3)
node.left=TreeNode(1)

var=Solution()
print(var.getMinimumDifference(node))
























# class TreeNode:
#     def __init__(self,x):
#         self.val=x
#         self.left=None
#         self.right=None
# class Solution():
#     def helper(self,root,value):
#         if root==None:
#             return
#         else:
#             self.helper(root.left,value)
#             value.append(root.val)
#             self.helper(root.right,value)
#         return value
#
#     def getMinimumDifference(self, root):
#         value=[]
#         ans=1000000
#         arra= self.helper(root,value)
#         for i in range(1,len(arra)):
#             ans=min(ans,arra[i]-arra[i-1])
#         return ans
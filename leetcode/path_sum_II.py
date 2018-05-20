
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def helper(self,root,sum,array,n,ans,target):
        if root==None:
            return
        else:
            if len(array)<=n:
                array.append(root.val)
            else:
                array[n]=root.val
            if sum+root.val==target:
                ans.append(array[:n+1])
            if root.left:
                self.helper(root.left,sum+root.val,array,n+1,ans,target)
            if root.right:
                self.helper(root.right,sum+root.val,array,n+1,ans,target)
        return ans


    def pathSum(self, root, sum):
        return  self.helper(root,0,[],0,[],sum)

var=TreeNode(5)
var.left=TreeNode(4)
var.right=TreeNode(8)
var.right.left=TreeNode(13)
var.right.right=TreeNode(4)
var.right.right.right=TreeNode(1)
var.right.right.left=TreeNode(5)
var.left.left=TreeNode(11)
var.left.left.left=TreeNode(7)
var.left.left.right=TreeNode(2)


p=Solution()
print(p.pathSum(var,22))

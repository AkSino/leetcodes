# Python program to print right view of Binary Tree

# A binary tree node
class Node:
    # A constructor to create a new Binary tree Node
    def __init__(self, item):
        self.data = item
        self.left = None
        self.right = None


# Recursive function to print right view of Binary Tree
# used max_level as reference list ..only max_level[0]
# is helpful to us

def printView(root,futureLevel,curlevel,fin_ans):
    if root==None:
        return
    else:
        if(futureLevel>curlevel[0]):
            fin_ans.append(root.data)
            curlevel[0]=futureLevel

        printView(root.right,futureLevel+1,curlevel,fin_ans)
        printView(root.left,futureLevel+1,curlevel,fin_ans)
    return fin_ans


def rightView(root):
    return printView(root,1,[0],[])


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)

print(rightView(root))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
























# class Tree():
#     def __init__(self,data):
#         self.data=data
#         self.right=None
#         self.left=None
#
# class Solution():
#     def rightSideView(self, root):
#         ans=[root.data]
#         while root.right or root.left:
#             if root.right:
#                 root=root.right
#                 ans.append(root.data)
#             elif root.left:
#                 root=root.left
#                 ans.append(root.data)
#
#         return ans
# tree=Tree(2)
# tree.left=Tree(4)
# tree.right=Tree(8)
# tree.left.right=Tree(7)
#
# var=Solution()
# print(var.rightSideView(tree))
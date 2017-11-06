#https://leetcode.com/problems/sum-root-to-leaf-numbers/description/

from Trees.Tree import Tree


vardan=Tree(2)
vardan.left=Tree(4)
vardan.right=Tree(6)
vardan.left.left=Tree(2)
vardan.left.right=Tree(3)
vardan.right.left=Tree(6)
vardan.right.right=Tree(9)


def FindNodeSum(root):
    list=[]
    if root==None:
        return [[]]
    if root.left==None and root.right==None:
        return [[root.data]]
    else:
        for i in FindNodeSum(root.left):
            list.append(i+[root.data])
        for j in FindNodeSum(root.right):
            list.append(j+[root.data])
    return list

print(FindNodeSum(vardan))




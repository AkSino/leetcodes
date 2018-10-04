import sys

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def arrayToTree(array):
    roots=TreeNode(array[0])
    arrays=[roots]
    i=1
    while i<len(array):
        root=arrays.pop(0)
        if(array[i]):
            root.left=TreeNode(array[i])
            arrays.append(root.left)
        else:
            root.left=None
        i+=1
        if(array[i]):
            root.right=TreeNode(array[i])
            arrays.append(root.right)
        else:
            root.right=None
        i+=1

    return roots

p=arrayToTree([3,2,3,None,3,None,1])

print(p)

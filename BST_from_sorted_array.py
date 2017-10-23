class Tree(object):
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def ArrayToTree(array,start,end):
    length=len(array)
    if start>end:
        return None
    if start==end:
        new_tree = Tree(array[start])
        return new_tree
    mid=start+end//2
    new_tree=Tree(array[mid])
    new_tree.left=ArrayToTree(array,start,mid-1)
    new_tree.right=ArrayToTree(array,mid+1,end)
    return new_tree

tree=ArrayToTree([1,2,3],0,2)

print(tree.left.data)


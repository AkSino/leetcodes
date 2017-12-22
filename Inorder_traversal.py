class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
arr=[]
def inorder(root):
    # if root.left==None :
    #     if root.key not in arr:
    #         arr.append(root.key)
    # else:
    #     inorder(root.left)
    # if root.key not in arr:
    #     arr.append(root.key)
    # if root.right==None:
    #     if root.key not in arr:
    #         arr.append(root.key)
    # else:
    #     inorder(root.right)
    if root==None:
        return
    inorder(root.left)
    inorder(root.right)
    arr.append(root.key)

    return arr


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(inorder(root))
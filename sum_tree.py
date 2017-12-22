class Node:
    # Constructor to create a new tree node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def findSumTree(root):
    if root==None:
        return True
    if root.left:
        a=findSumTree(root.left)
    if root.right:
        b=findSumTree(root.right)
    if root.key==getSumFromroot(root) and a and b:
        return True
    else:
        return False


def getSumFromroot(root):
    if root==None:
        return 0
    summing=0
    if root.left:
        summing=summing+root.left.key+getSumFromroot(root.left)
    if root.right:
        summing = summing + root.right.key + getSumFromroot(root.right)
    return summing

root = Node(3)
root.left = Node(2)
root.right = Node(1)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right.left = Node(6)
# root.right.right = Node(7)

print(findSumTree(root))
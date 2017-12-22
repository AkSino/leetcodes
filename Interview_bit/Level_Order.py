class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printLevel(root):
    evenStack=[]
    oddStack=[]
    if root:
        evenStack.append(root)
    else:
        return []
    even=1
    ans=[]
    while evenStack or oddStack:
        if even==1:
            internal=[]
            while evenStack:
                a=evenStack.pop(0)
                internal.append(a.data)
                if a.left:
                    oddStack.append(a.left)
                if a.right:
                    oddStack.append(a.right)
            even=0
            ans.append(internal)
        else:
            internal = []
            while oddStack:
                a=oddStack.pop(0)
                internal.append(a.data)
                if a.left:
                    evenStack.append(a.left)
                if a.right:
                    evenStack.append(a.right)
            even=1
            ans.append(internal)
    return ans


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(printLevel(root))
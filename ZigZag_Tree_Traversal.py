class Node():
    def __init__(self,key):
        self.key=key
        self.left=None
        self.right=None
stack=[]
def printZigZag(root):
    evenStack=[]
    oddStack=[]

    if root==None:
        return
    else:
        evenStack.append(root)

    evenStage=True

    while(len(evenStack)!=0 or len(oddStack)!=0):
        if evenStage:
            while len(evenStack)!=0:
                p=evenStack.pop(0)
                print(p.key)
                if p.left != None:
                    oddStack.insert(0, p.left)
                if p.right!=None:
                    oddStack.insert(0,p.right)

            evenStage=False
        else:
            while(len(oddStack))!=0:
                p=oddStack.pop(0)
                print(p.key)
                if p.right != None:
                    evenStack.insert(0, p.right)
                if p.left!=None:
                    evenStack.insert(0,p.left)

            evenStage=True

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

printZigZag(root)





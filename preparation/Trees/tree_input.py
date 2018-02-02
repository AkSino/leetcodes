class Node():
    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

class Tree():
    def formTree(self):
        stack=[]
        elem=int(input("Enter root Element"))
        root=Node(elem)
        stack.append(root)
        while stack:
            elem=stack.pop(0)
            lefty=int(input("Enter left element of " + str(elem.data)))
            righty=int(input("Enter right element of " + str(elem.data)))
            if lefty !=(-1):
                elem.left=Node(lefty)
                stack.append(elem.left)
            if righty!=(-1):
                elem.right=Node(righty)
                stack.append(elem.right)
        return root
var=Tree()



class Print():
    def __init__(self):
        self.arr=[]
    def inorder(self,root):
        if root==None:
            return
        self.inorder(root.left)
        self.arr.append(root.data)
        self.inorder(root.right)

        return self.arr


var2=Print()

if __name__ == '__main__':
    a = var.formTree()
    print(var2.inorder(a))

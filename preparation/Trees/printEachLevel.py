class Tree():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def printLayers(root):
    even = []
    odd = []
    even.append(root)

    while len(even) != 0 or len(odd) != 0:
        if len(even) != 0:
            while len(even) != 0:
                node = even.pop(0)
                print(node.data, end="")
                if node.left:
                    odd.append(node.left)
                if node.right:
                    odd.append(node.right)
            print("even")

        if len(odd) != 0:
            while len(odd) != 0:
                node = odd.pop(0)
                print(node.data, end="")
                if node.left:
                    even.append(node.left)
                if node.right:
                    even.append(node.right)
            print("odd")


var = Tree(1)
var.left = Tree(2)
var.right = Tree(3)
var.left.left = Tree(4)
var.left.right = Tree(6)

printLayers(var)

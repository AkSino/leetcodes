class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


def removeNode(root,datas):
    if root.next==None:
        if root.data==datas:
            return None
        else:
            return root
    pseudo=Node(0)
    pseudo.next=root
    pseudoPointer=pseudo
    # pseudo.next=pseudoPointer
    while pseudoPointer and pseudoPointer.next:
        if pseudoPointer.next.data==datas:
            pseudoPointer.next=pseudoPointer.next.next
        else:
            pseudoPointer=pseudoPointer.next
    return root


tree=Node(1)
tree.next=Node(2)
tree.next.next=Node(2)
a=removeNode(tree,2)
while a:
    print(a.data)
    a=a.next



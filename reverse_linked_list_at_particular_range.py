class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


def ReverseList2(root,m,n):
    dummy=Node(9)
    dummy.next=root
    p=dummy
    p2=root
    for i in range(0,m):
        p=p.next
        p2=p2.next
    turn_node=p2
    prev=None
    current=p2
    for o in range(n-m+1):
        nexti=current.next
        current.next=prev
        prev=current
        current=nexti
    p.next=prev
    turn_node.next=current

    return dummy.next




a=Node(1)
a.next=Node(2)
a.next.next=Node(3)
a.next.next.next=Node(4)
a.next.next.next.next=Node(5)

a=ReverseList2(a,1,3)
print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)
print(a.next.next.next.next.data)
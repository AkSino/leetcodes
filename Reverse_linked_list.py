class Node():
    def __init__(self,data):
        self.data=data
        self.next=None

def ReverseList(root):
    prev=None
    current=root
    while current:
        pointer1=current.next
        current.next=prev
        prev=current
        current=pointer1
    return prev

a=Node(1)
a.next=Node(2)
a.next.next=Node(3)
a.next.next.next=Node(4)
a.next.next.next.next=Node(5)

a=ReverseList(a)
print(a.data)
print(a.next.data)
print(a.next.next.data)
print(a.next.next.next.data)
print(a.next.next.next.next.data)
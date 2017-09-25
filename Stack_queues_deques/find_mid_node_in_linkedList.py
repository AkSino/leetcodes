class LinkedList(object):
    def __init__(self,value):
        self.value=value
        self.nextNode=None

a=LinkedList(20)
b=LinkedList(30)
c=LinkedList(40)
d=LinkedList(50)
e=LinkedList(60)

a.nextNode=b
b.nextNode=c
c.nextNode=d
d.nextNode=e


pointer1=a
pointer2=a

while pointer1!=None and pointer1.nextNode!=None:
    pointer1=pointer1.nextNode.nextNode
    pointer2=pointer2.nextNode

print(pointer2.value)
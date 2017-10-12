class Node(object):
    def __init__(self,data):
        self.next=None
        self.data=data

class LinkedList(object):
    def __init__(self):
        self.head=None

    def totalNodes(self):
        i=self.head
        p=0
        while i.next:
            i=i.next
            p+=1
        return p+1

    def push(self,elem):
        new_node=Node(elem)
        new_node.next=self.head
        self.head=new_node

    def printList(self):
        startPointer=self.head
        while startPointer != None:
            print(startPointer.data)
            startPointer=startPointer.next

    def reverseList(self):
        current=self.head
        prev=None
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        self.head=current

    def k_swap(self,k):
        current=self.head
        prev=None
        num=int(self.totalNodes()/k)
        for i in range(0,num):

            for j in range(k):
                next=current.next
                current.next=prev
                prev=current
                current=next
                j+=1
            i+=1




vardan=LinkedList()
vardan.push(21)
vardan.push(32)
vardan.push(21)
vardan.push(32)
vardan.push(21)
vardan.push(32)

vardan.printList()
print(vardan.totalNodes())
vardan.k_swap(2)
vardan.printList()

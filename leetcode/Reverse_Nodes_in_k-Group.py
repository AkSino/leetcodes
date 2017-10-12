#https://leetcode.com/problems/reverse-nodes-in-k-group/description/
class LinkedList(object):
    def __init__(self,data):
        self.nextNode=None
        self.data=data

    def printVal(self):
        return self.data

q1=LinkedList(3)
q2=LinkedList(4)
q3=LinkedList(3)
q4=LinkedList(4)

q1.nextNode=q2
q2.nextNode=q3
q3.nextNode=q4

print(q2.nextNode.printVal())

pointer1=q1
pointer2=pointer1.nextNode
pointer3=None
while pointer1.nextNode != None and pointer2.nextNode!=None:
    pointer3=pointer2.nextNode
    pointer2.nextNode=pointer1
    pointer1=pointer2
    pointer2=pointer3

print(q2.nextNode.printVal())






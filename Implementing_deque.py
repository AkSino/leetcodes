#Dequeue is a hybrid datastructure, basically in which we et both the properties of stack and queue. We can add or remove elements
#from front as well as from the starting.


class Deque(object):
    def __init__(self):
        self.deque=[]

    def addFront(self,elem):
        self.deque.append(elem)

    def addRear(self,elem):
        self.deque.insert(0,elem)

    def removeFront(self):
        return self.deque.pop()

    def removeRear(self):
        return self.deque.pop(0)

    def isEmpty(self):
        return self.deque == []

    def size(self):
        return (len(self.deque))
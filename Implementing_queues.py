class Queues(object):
    def __init__(self):
        self.queue=[]

    def enqueue(self,element):
        self.queue.insert(0,element)

    def dequeue(self):
        self.queue.pop()

    def IsEmpty(self):
        return self.queue==[]


test=Queues()
test.enqueue(3)


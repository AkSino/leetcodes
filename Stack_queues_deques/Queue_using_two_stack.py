class DoubleStack(object):
    def __init__(self):
        self.instack=[]
        self.outstack=[]

    def Enqueue(self,elem):
        self.instack.append(elem)

    def Dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

vardan=DoubleStack()
vardan.Enqueue(2)
vardan.Enqueue(4)
print(vardan.Dequeue())
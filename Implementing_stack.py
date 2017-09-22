class Stack(object):
    def __init__(self):
        self.stack=[]

    def push(self,element):
        self.stack.append(element)

    def IsEmpty(self):
        return self.stack == []

    def pop(self):
        self.stack.pop()


test=Stack()
try:
    test.pop()
except Exception:
    print("There is no item in Stack to pop")

test.push("Vardan")
print(test.IsEmpty())
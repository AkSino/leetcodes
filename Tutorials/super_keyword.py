class A():
    def __init__(self):
        print("Inside A")
        self.M="VARDAN"

class B(A):
    def __init__(self):
        super().__init__()
        print("Inside B")
        print(self.M)
var=B()



#If we use super(current_or_parent_class_name, self).__init__(), then it will call the init method of parent of class used inside super.
class A():
    def __init__(self):
        print("A")

class C(A):
    def __init__(self):
        # super(B,self).__init__()
        print("C")
class B(C):
    def __init__(self):
        super(B,self).__init__()
var=B()

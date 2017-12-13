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

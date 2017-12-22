vardaan = 15
def a(vardan):
    vardaan = 10
def m():
    print(vardaan)
    a(vardaan)
    print(vardaan)
m()


#If we use global then value changes
class Vardan():
    def A(self):
        global a
        a=20

var=Vardan()
a=10
print(a)
var.A()
print(a)
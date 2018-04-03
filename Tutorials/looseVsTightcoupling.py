#Example of tight coupling. Tight coupling is bad in any programming language. It means dependency among the classes. One class can change variable
#
class class1():
    def __init__(self):
        self.name="VARDAN"
    def changeName(self):
        self.name="ADIT"


vardan=class1()
print(vardan.name)
vardan.changeName()
print(vardan.name)

class class2():
    def __init__(self):
        self.__name="VARDAN"
    def changeName(self):
        self.__name="ADIT"
    def getName(self):
        return self.__name

vardan2=class2()
print(vardan2.getName())
vardan2.changeName()
print(vardan2.getName())
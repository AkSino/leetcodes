class Student:
    def __init__(self,name,roll,age):
        self.name=name
        self.roll=roll
        self.age=age
    def count(self):
        print (self.name)
        print(self.roll)


vardan=Student("VARDAN",987248,34)

vardan.count()
vardan.name
print(vardan.age)
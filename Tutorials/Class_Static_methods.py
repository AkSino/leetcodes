#We can use class methods as alternative constructors. A class method is a function that is a function of the class.
#  It accepts the class as an argument to it.

class Student(object):
    def __init__(self,name,roll):
        self.name=name
        self.roll=23

    @classmethod
    def alternate_const(cls,name,roll):   #Here cls is referring to the class itself directly.
        return cls(name,roll)
    @classmethod
    def change_roll(cls,roll):
        cls.roll=roll

var=Student.alternate_const("Vardan",123)
print(var.roll)

#We can also change the defined variables inside the class permanently for all the objects

Student.change_roll(223)
print(Student.roll)
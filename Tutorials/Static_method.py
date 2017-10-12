#Static method dont pass the instance or class like instance or class methods.


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

#We dont need to instantiate the static method of class. We can call them as it is.

    @staticmethod
    def is_workday(day):
        if day==2:
            print("YES")
        else:
            print("NO")

var=Student.alternate_const("Vardan",123)
print(var.roll)

#We can also change the defined variables inside the class permanently for all the objects

Student.change_roll(223)
print(Student.roll)

Student.is_workday(3)
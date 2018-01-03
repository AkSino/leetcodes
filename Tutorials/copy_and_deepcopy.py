#In case of deep copy, a copy of object is copied in other object. It means that any changes made to a copy of object do not reflect in the original object.

#In case of shallow copy, a reference of object is copied in other object. It means that any changes made to a copy of object do reflect in the original object.

#basically in deepcopy whole new objects are created with the same value as the parent object while in shallow copy just the reference to the parent object is given
#to the new object created.

#The clone() method saves the extra processing task for creating the exact copy of an object.
#If we perform it by using the new keyword, it will take a lot of processing to be performed that is why we use object cloning.
import copy

class Vardan():
    def __init__(self,data):
        self.data=data

    def printData(self):
        print(self.data)

var=Vardan(29)
dan=copy.copy(var)
dan.data=45
var.printData()
dan.printData()

a=[1,2,3]
b=copy.deepcopy(a)

b[2]=4

print(b)
print(a)
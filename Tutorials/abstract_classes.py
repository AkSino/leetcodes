#Abstract classes are classes that contain one or more abstract methods.
# An abstract method is a method that is declared, but contains no implementation.
# Abstract classes may not be instantiated, and require subclasses to provide implementations for the abstract methods.
# Subclasses of an abstract class in Python are not required to implement abstract methods of the parent class.

#Abstract classes inherits the ABC class and decorators are used to tell python that a function is abstract function

from abc import ABC, abstractmethod

class A(ABC):

    @abstractmethod
    def xyz(self):
        pass

class B(A):
    def pqr(self):
        pass

var=B()
var.pqr()

#This will throw an error in python. To make this thing work, we have to use the xyz function in the B class's object

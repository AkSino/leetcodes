from Tutorials import classmethod_tutorial

#whenever python starts the execution, it sets few variables like __name__.

print(__name__)

#If we import some file, python will execute its code. For example we imported classmethod_tutorials and its code has been executed.

print(classmethod_tutorial.__name__)

#Thats why we use below

if __name__ =="__main__":
    #some_method_for_execution
    pass
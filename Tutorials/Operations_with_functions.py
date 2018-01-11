#First Class functions allows us to treat functions like any other object so for example we can pass functions to another
# function, we can retire cut up and we can assign functions to variables. now closures allow us to take advantage of first
# class functions and return and enter function that remembers and has access to variables local to the store in which they were created
def outer_function():
    print("VARDAN")

#We can store the function name into the variable. If we use bracket then it means we are calling the function. But to store the
#function as a variable we dont have to use the bracket.

#A Closure is a function object that remembers values in enclosing scopes even if they are not present in memory.

vardan=outer_function
vardan()

#We can also return the functions
#Here also we dont have to use the brackets
def function2():
    return outer_function


#We can also define global variable from inside a function.

#What is a decorator decorator is just a function that takes function as an argument and then returns another function.
# this without altering the source code of the original function that you passed in


#so decorating our functions allows us to easily add functionality to our existing functions adding that functionality inside of wrapper
# without modifying our original display function
def decorator_function(function_as_parameter):
    def wrapper_function():
        print("THIS IS THE ADDITIONAL FUNCTIONALITY ADDED WITHOUT MODIFYING THE ORIGINAL FUNCTION")
        return function_as_parameter()
    return wrapper_function

def display():
    print("VARDAN")

decorated_display=decorator_function(display)
decorated_display()

#The above code can be used as below also using the decorator.
def decorator_function(function_as_parameter):
    def wrapper_function():
        print("THIS IS THE ADDITIONAL FUNCTIONALITY ADDED WITHOUT MODIFYING THE ORIGINAL FUNCTION")
        return function_as_parameter()
    return wrapper_function

@decorator_function
def display():
    print("VARDAN")

display()


#Now if we want to make a functionality to work with any of the existing function, we need to use args and kwargs in the decorator function.
def decorator_function(function_as_parameter):
    def wrapper_function(args,*kwargs):
        print("THIS IS THE ADDITIONAL FUNCTIONALITY ADDED WITHOUT MODIFYING THE ORIGINAL FUNCTION")
        return function_as_parameter(args,*kwargs)
    return wrapper_function
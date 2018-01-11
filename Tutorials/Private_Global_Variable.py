#_variable means protected
#__variable means private

#But There is not such an exact concept of private or protected variable in python, its just that we use it so that
#  whenever some other developer is using that variable
# we can pinpoint in by seeing the underscores (_ for protected and __ for private) and the other developer makes sure to not to use those variable.

#We can still access the private and protected variables although the good practice is using the getters and setters.

#Private
class Testing(object):
   __var=True
   dan=False
   def accessible(self):
       print(Testing.__var)

vardan=Testing()
print(vardan.__var)

#It will not print the value of __var. If we replace the last line with below line it will print.
print(vardan._Testing.__var)
#or we can use below
vardan.accessible()



#For protected:

class Testing(object):
   _var=True
   dan=False
   def accessible(self):
       print(Testing.__var)

vardan=Testing()
print(vardan._var)
#or we can use below
vardan.accessible()

#It will print (_var).

#We should always create getters and setters to access such variables.

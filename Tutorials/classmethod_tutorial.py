class A():
    #These are the class variable
    interest=10
    def change_interest(self,data):
        #this is the instance variable
        self.interest=20

    @classmethod
    def change_using_classmethod(cls):
        cls.interest=50

vardan=A()
# print(vardan.interest)
vardan.change_interest(39)
print(vardan.interest)
vardan2=A()
print(vardan2.interest)
#Above code changes the value of interest for vardan only and not for vardan2. Thats why we use class methods
print(vardan2.interest)
print(vardan.interest)
A.change_using_classmethod()
print(vardan2.interest)
#The line below is representing the instance variable and so it is printing 10 instead of 50. We have made change to class variable
#in the line line A.change_using_classmethod()

print(vardan.interest)
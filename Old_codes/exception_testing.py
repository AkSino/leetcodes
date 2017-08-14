age=35
#if (age<100):
#    raise NameError()



def Accident(Exception):
    def __init__(self,name):
        self.name=name
    def print_name(self):
         print (self.name)


try:
    if(age<100):
        raise Accident

except Accident():
     Accident("Accident").print_name
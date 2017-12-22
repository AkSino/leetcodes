def method(*args):
    for each in args:
        print(each)

method(1,2,3,4)

def method_kwarg(**kwargs):
    for each,value in kwargs.items():
        print(each,value)

method_kwarg(name="VARDAN",age=24,sex="M")
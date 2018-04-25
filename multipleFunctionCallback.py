methods=[]

def addMeth(meth):
    methods.append(meth)

def performMethod():
    for each in range(len(methods)):
        methods[each]()
    methods.clear()

def meth():
    print("njnrj")

addMeth(meth)
addMeth(meth)
addMeth(meth)

performMethod()
def meth(a, b):
    x=a
    y=b
    if(a==b):
        print(a)
    else:
        if(x>y):
            x=x-y
        elif(x<y):
            y=y-x

        meth(x, y)


meth(2437, 875)

a=set()
a.add((1,2))
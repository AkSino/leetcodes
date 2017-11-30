def first_decorator(f):
    def changeCase(*args,**kwargs):
        x=f(*args,**kwargs)
        return x.lower()
    def changeCase2(*args,**kwargs):
        x=f(*args,**kwargs)
        return x.upper()

    return changeCase2()

@first_decorator
def xyz():
    return "VARDaN"

print(xyz())
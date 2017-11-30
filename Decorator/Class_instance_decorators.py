class decorator_instance(object):
    def __init__(self):
        self.tracing=True
    def __call__(self,f):
        def wrap(*args,**kwargs):
            if self.tracing:
                print("VARDAsN")
            return f(*args,**kwargs)
        return wrap
var=decorator_instance()
@var
def xyz():
    print("VARDAN")

xyz()
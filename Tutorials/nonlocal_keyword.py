
def findCycle():
    def func():
        nonlocal a
        a = 20
    a=10
    print(a)
    func()
    print(a)

findCycle()
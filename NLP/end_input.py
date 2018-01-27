import atexit
s=0
@atexit.register
def quit_gracefully():
    global s
    print ('Bye')
    x=1


atexit.register(quit_gracefully)


while True:
    if s==1:
        break
    a=input()

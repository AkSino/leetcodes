import threading

lock = threading.RLock()

def meth(i):
    if i==0:
        print("Reached till this point")
        return
    print ('First try :', lock.acquire())
    i-=1
    meth(i)
    print(lock.release())
    return

meth(4)
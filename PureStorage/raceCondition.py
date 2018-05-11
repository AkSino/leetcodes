import threading


global a
a=10

import threading


def add():
    global a
    for i in range(1000000):
        a+=1

def add2():
    global a
    for i in range(1000000):
        a+=1

thread=threading.Thread(target=add)
thread2=threading.Thread(target=add2)
thread.start()
thread2.start()
thread.join()
thread2.join()

print(a)


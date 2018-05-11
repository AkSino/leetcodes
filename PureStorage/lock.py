import threading


global a
a=10
def add():
    global a
    global locke
    global locke2
    for i in range(10000):
        locke.acquire()
        try:
            a+=1
            locke2.aquire()

        finally:
            locke.release()
            try:
                a+=1
            finally:
                #pass
                locke2.release()


def add2():
    global locke
    global locke2
    global a
    for i in range(10000):
        locke.acquire()
        try:
            a+=1
            locke2.aquire()
        finally:
            locke.release()
            try:
                a += 1
            finally:
                #pass
                if locke2.locked():
                    locke2.release()



locke = threading.Lock()
locke2 = threading.Lock()

thread=threading.Thread(target=add)
thread2=threading.Thread(target=add2)
thread.start()
thread2.start()
thread.join()
thread2.join()

print(a)


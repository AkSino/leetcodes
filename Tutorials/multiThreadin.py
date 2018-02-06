#Thought of different programs running together but with ease of sharing of data
import threading
import time
def vrdan():
    while True:
        time.sleep(0.4)
        print("ekcne")
def attu():
    while True:
        time.sleep(0.2)
        print("papapapapa")
t=threading.Thread(target=vrdan)
t2=threading.Thread(target=attu)
t.start()
t2.start()
t.join()
t2.join()

#We can aquire and release the locks so that only particular thread can be in opearation.

#Python works on GIL Global Interpreter Lock which restricts it to use on more than one CPU or multiple cores.

#Python creates a data structure  containing interpreter state
#A new thread is laundhed
#Only one thread is being executed in python
#Whenever any I/O operation takes place, C code in python is written in such a way that it releases the GIL and threads execution takes place.

#https://www.youtube.com/watch?v=ph374fJqFPE




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




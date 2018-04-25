import threading
import time
import asyncio
user=[1,2]

async def addUser(data):
    time.sleep(1000)
    user.append(data)

async def getUser():
    time.sleep(20)
    print(user)
    await addUser()

t1=threading.Thread(target=addUser(4))
t2=threading.Thread(target=getUser())
t1.start()
t2.start()
t1.join()
t2.join()
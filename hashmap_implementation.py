class Hashmap():
    def __init__(self):
        self.array=[None for i in range(256)]
    def add(self,key,value):
        self.array[key%256]=value
    def get(self,key):
        if self.array[key%256]:
            print(self.array[key%256])
        else:
            print("No Value found")
            return

hash=Hashmap()

hash.add(2,"BHBH")
(hash.get(2))
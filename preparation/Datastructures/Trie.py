class Node():
    def __init__(self):
        self.terminate=False
        self.dict={}
        self.next=None

class Trie():
    def __init__(self):
        self.root=Node()

    def add(self,data):
        word=self.root
        for each in data:
            if each in self.root:
                self.add()
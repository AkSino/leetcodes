class Animal:
    def __init__(self,bark):
        self.bark=bark
    def barking(self):
        print(self.bark)
dog=Animal("YES")
dog.barking()

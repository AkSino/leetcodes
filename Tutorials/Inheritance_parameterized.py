class Animal():
    def __init__(self):
        print("From parent")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("From Dog")


vardan=Dog()

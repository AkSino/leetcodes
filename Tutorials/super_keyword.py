class Animal():
    def walk(self):
        print("Running")


class Bird(Animal):
    def walk(self):
        super().walk()
        print("Flying")



var=Bird()
var.walk()